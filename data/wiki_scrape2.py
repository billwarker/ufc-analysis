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
ufc_page = "/wiki/UFC_"
event_nums = range(1, 233)
more_events = True

with open("data/wiki_data2.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    for num in event_nums:
        url = wiki_url + ufc_page + str(num)
        infobox_rows = get_event_infobox_rows(url)
        event_data = get_event_data(infobox_rows)
        event = Event(event_data)
        print(event.title)
        writer.writerow(event.return_data())