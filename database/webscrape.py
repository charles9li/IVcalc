import requests
import urllib.request
import time
from bs4 import BeautifulSoup


def print_child_names(item):
    for child in item.children:
        print(child.name)


url = "https://serebii.net/pokedex-sm/001.shtml"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')
table = soup.body.find_all('table')[1]
body = table.find('tbody')
row = body.contents[2]
data = row.contents[3]
font = data.font
div = font.contents[2]
div = div.div
p = div.p
table = p.table
tbody = table.tbody
row = tbody.contents[2]
name = row.contents[3].text
