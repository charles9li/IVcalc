import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from database.webscrape_utils import PokemonInfo


for i in range(1, 810):
    pokemon = PokemonInfo(i)
    print(str(pokemon.number) + " " + pokemon.name)
