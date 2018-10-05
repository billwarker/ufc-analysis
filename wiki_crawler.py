import requests
from bs4 import BeautifulSoup
import csv
import numpy as np

def get_event_infobox_rows(url):
    r = requests.get(url)
    bs_obj = BeautifulSoup(r.text, "lxml")
    infoboxes = bs_obj.select("table.infobox")
    if len(infoboxes) == 1: # Ultimate Fighter pages have 2 infoboxes
        infobox = infoboxes[0].select_one("tbody")
    else:
        infobox = infoboxes[-1].select_one("tbody")

    infobox_rows = infobox.select("tr")
    return infobox_rows

def get_event_data(infobox_rows):
    title = infobox_rows[0].text
    event_data = {}
    event_data["Title"] = title
    for row in infobox_rows[:-3]:
        try:
            header = row.select_one("th").text
            data = row.select_one("td").text.replace('\n', '')
            event_data[header] = data
        except AttributeError:
            continue
    
    return event_data

def get_next_event_page(infobox_rows):
    try:
        next_event_page = infobox_rows[-1].select("td")[2].select_one('a')['href']
        return next_event_page
    except TypeError:
        global more_events
        more_events = False
        return ''
        

class Event:
    def __init__(self, event_data):
        self.title = event_data["Title"]
        self.promotion = event_data["Promotion"]
        self.date = event_data["Date"]
        self.venue = event_data["Venue"]
        self.city = event_data["City"]
        try:
            self.attendance = event_data["Attendance"]
        except KeyError:
            self.attendance = np.NaN
        try:
            self.total_gate = event_data["Total gate"]
        except KeyError:
            self.total_gate = np.NaN
        try:
            self.buyrate = event_data["Buyrate"]
        except KeyError:
            self.buyrate = np.NaN
    def return_data(self):
        return [self.title, self.promotion,
                self.date, self.venue,
                self.city, self.attendance,
                self.total_gate, self.buyrate]
    
    
wiki_url = 'https://en.wikipedia.org'
ufc_debut_page = "/wiki/UFC_1"
more_events = True

with open("ufc_data.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    url = wiki_url + ufc_debut_page
    while more_events:
        infobox_rows = get_event_infobox_rows(url)
        event_data = get_event_data(infobox_rows)
        event = Event(event_data)
        print(event.title)
        writer.writerow(event.return_data())
        
        next_event_page = get_next_event_page(infobox_rows)
        if more_events:
            url = wiki_url + next_event_page
        else:
            break