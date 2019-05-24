import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from database.webscrape_utils import PokemonInfo


def print_child_names(item):
    for child in item.children:
        print(child.name)


pokemon = PokemonInfo(1)
# print_child_names(pokemon._stats_tag().parent.parent.parent.contents[3])
print(pokemon._stats_tag().parent.parent.parent.contents[3].contents[2])
