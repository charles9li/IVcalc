import requests
from bs4 import BeautifulSoup


def _info_general(number):
    """
    Returns BeautifulSoup instance of containing general Pokémon info.

    :param number: Pokédex number
    :return: BeautifulSoup instance containing general Pokémon info
    """
    soup = _url_to_soup(number)
    table = soup.body.find_all('table')[1]
    tbody = table.find('tbody')
    row = tbody.contents[2]
    data = row.contents[3]
    font = data.font
    div = font.contents[2]
    div = div.div
    p = div.p
    return p


def _url_to_soup(number):
    """
    Returns BeautifulSoup instance of the parsed Pokédex page.

    :param number: Pokédex number
    :return: BeautifulSoup instance containing parsed Pokédex page
    """
    url = _number_to_url(number)
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html5lib')


def _number_to_url(number):
    """
    Returns the url of the Pokédex page for a given Pokédex number.

    :param number: Pokédex number
    :return: url of Pokédex page
    """
    num_string = _dex_number(number)
    return "https://serebii.net/pokedex-sm/" + num_string + ".shtml"


def _dex_number(number):
    """
    Converts an integer number to a 3-digit string.

    :param number: Pokédex number
    :return: dex number in the form of a 3-digit string
    """
    number = str(number)
    while len(number) < 3:
        number = '0' + number
    return number
