import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from database.webscrape_utils import *


p = info_general(1)
table = p.table
tbody = table.tbody
row = tbody.contents[2]
name = row.contents[3].text
print(name)
