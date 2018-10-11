import pandas as pd
import numpy as np
import re
from datetime import datetime

### Load as Dataframe

columns = ['Event', 'Promotion', 'Date', 'Venue', 'City', 'Attendance', 'Gate', 'Buyrate']
wiki_df = pd.read_csv("ufc_data.csv", names=columns)

### Clean Dates

date_p1 = re.compile("([A-Z][a-z]*) ([0-9]+), ([0-9]+)")
date_p2 = re.compile("([0-9]+) ([A-Z][a-z]*) ([0-9]+)")

def clean_date(date):

    date = date.replace("\xa0", ' ')
    
    if date_p1.match(date):
        chunk = date_p1.findall(date)[0]
        clean_string = "{} {} {}".format(chunk[0], chunk[1], chunk[2])    
    elif date_p2.match(date):
        chunk = date_p2.findall(date)[0]
        clean_string = "{} {} {}".format(chunk[1], chunk[0], chunk[2])
    elif date == 'Cancelled':
        return date
        
    dt_object = datetime.strptime(clean_string, "%B %d %Y").date()
    return dt_object

wiki_df['Date'] = wiki_df['Date'].apply(clean_date)
wiki_df = wiki_df[wiki_df['Date'] != 'Cancelled']

### Clean Buyrate

buy_p1 = re.compile("([0-9]+,[0-9]+,*[ ]*[0-9]*)")

def clean_buyrate(buyrate):
    try:
        if buy_p1.match(buyrate):
            chunk = buy_p1.findall(buyrate)[0]
            clean_string = "{}".format(chunk).replace(',','')
            return int(clean_string)
        else:
            print(buyrate)
    except TypeError:
        pass # so we don't print out NaNs

wiki_df['Buyrate'] = wiki_df['Buyrate'].apply(clean_buyrate)

### Clean Gate

gate_p1 = re.compile("\$([0-9]+,[0-9]*,*[0-9]*)")
gate_p2 = re.compile("\$([0-9]\.[0-9]+)")

def clean_gate(gate):
    try:
        if gate_p1.match(gate):
            chunk = gate_p1.findall(gate)[0]
            clean_string = "{}".format(chunk).replace(',','')
            return int(clean_string)
        elif gate_p2.match(gate):
            chunk = gate_p2.findall(gate)
            gate_num = float(chunk) * 1000000
            print(gate_num)
            return int(gate_num)
        else:
            print(gate)
    except TypeError:
        pass # so we don't print out NaNs

wiki_df['Gate'] = wiki_df['Gate'].apply(clean_gate)

### Clean Attendance

attend_p1 = re.compile("([0-9]+,*[0-9]*)")

def clean_attendance(attend):
    if '♠' in str(attend):
        attend = attend.split('♠')[1]
    try:
        if attend_p1.match(attend):
            chunk = attend_p1.findall(attend)[0]
            clean_string = chunk.replace(',','')
            return int(clean_string)
        else:
            print(attend)
    except TypeError:
        pass # so we don't print out NaNs

wiki_df['Attendance'] = wiki_df['Attendance'].apply(clean_attendance)
wiki_df = wiki_df.set_index(pd.DatetimeIndex(wiki_df['Date']))
wiki_df.drop('Date', axis=1, inplace=True)

### Fill missing Buyrates with Tapology Dataset

tap_df = pd.read_csv("tapology_data.csv")

def clean_tap_buyrate(buyrate):
    return int(buyrate.replace(',', '').replace('\n', ''))

tap_df['Buyrate'] = tap_df['Buyrate'].apply(clean_tap_buyrate)

def clean_tap_date(date):
    return datetime.strptime(date, "%Y.%m.%d").date()

tap_df['Date'] = tap_df['Date'].apply(clean_tap_date)
tap_df = tap_df.set_index(pd.DatetimeIndex(tap_df['Date']))

wiki_df['Buyrate'] = wiki_df['Buyrate'].fillna(tap_df['Buyrate'])

## Extract Features

data = wiki_df

### Extract Event and Title

def extract_title(event):
    if ': ' in event:
        event_name, title_name = event.split(': ', maxsplit=1)
        return title_name
    else:
        return np.nan

def extract_event(event):
    if ': ' in event:
        event_name, title_name = event.split(': ', maxsplit=1)
        return event_name
    else:
        return event

titles = data['Event'].apply(extract_title)
data.insert(1, 'Title', titles)
data['Event'] = data['Event'].apply(extract_event)

### Extract Fighter Names from Title

fighter2_p = re.compile("(.+) [Finale|[0-9]]*")

def extract_fighter1(title):
    if ' vs ' in str(title):
        title = title.replace(' vs ', ' vs. ')
    if ' vs. ' in str(title):
        fighter1 = title.split(' vs. ')[0]
        return fighter1
    
def _drop_roman_nums(string):
    if string.endswith(' II'):
        return string.replace(' II', '')
    elif string.endswith(' III'):
        return string.replace(' III', '')
    else:
        return string
    
def extract_fighter2(title):
    if ' vs ' in str(title):
        title = title.replace(' vs ', ' vs. ')
    if ' vs. ' in str(title):
        fighter2 = title.split(' vs. ')[1]
        if fighter2_p.match(fighter2):
            return _drop_roman_nums(fighter2_p.findall(fighter2)[0])
        return _drop_roman_nums(fighter2)

fighter1 = data['Title'].apply(extract_fighter1)
data.insert(3, "Fighter_1", fighter1)

fighter2 = data['Title'].apply(extract_fighter2)
data.insert(4, "Fighter_2", fighter2)

data = data.set_value('2006-10-10', 'Fighter_2', 'Shamrock')

### Extract Rematches

def extract_rematch(title):
    title = str(title)
    if ('2' in title) or ('3' in title) or ('II' in title) or ('III' in title):
        return 1
    else:
        return 0

rematch = data['Title'].apply(extract_rematch)
data.insert(5, "Rematch", rematch)

### Extract Main Events

main_event_p = re.compile("UFC [0-9]+")
main_event = data['Event'].apply(lambda x: 1 if main_event_p.match(x) else 0)

data.insert(1, 'Main_Event', main_event)

data.to_csv("ufc_clean.csv")