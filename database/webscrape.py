import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from database.webscrape_utils import PokemonInfo


def print_child_names(item):
    for child in item.children:
        print(child.name)


pokemon = PokemonInfo(25)
print(pokemon.base_stats)
