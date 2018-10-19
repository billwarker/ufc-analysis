import requests
from bs4 import BeautifulSoup
import csv
import numpy as np

def get_table_rows(url):
    r = requests.get(url)
    bs_obj = BeautifulSoup(r.text, "lxml")
    table = bs_obj.select_one("table.siteSearchResults")
    table_rows = table.select("tr")
    return table_rows

def get_row_data(row):
    row_data = {}
    columns = row.select("td")
    row_data['Event'] = columns[0]
    row_data['Title'] = columns[2]
    row_data['Date'] = columns[4]
    row_data['Buyrate'] = columns[6]
    return row_data


class Event:
    def __init__(self, row_data):
        self.event = row_data["Event"].text
        self.title = row_data["Title"].text
        self.date = row_data["Date"].text
        self.buyrate = row_data["Buyrate"].text
    def return_data(self):
        return [self.event, self.title,
                self.date, self.buyrate]


url = 'https://www.tapology.com/search/mma-event-figures/ppv-pay-per-view-buys-buyrate'

with open("data/tapology_data.csv", "w+", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['Event', 'Title', 'Date', 'Buyrate'])
    table_rows = get_table_rows(url)
    for row in table_rows[1:]:
        row_data = get_row_data(row)
        event = Event(row_data)
        print(event.title)
        writer.writerow(event.return_data())