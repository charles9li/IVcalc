import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'https://serebii.net/pokedex-sm/001.shtml'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.body.find_all('table')[1].find_all('tr'))
