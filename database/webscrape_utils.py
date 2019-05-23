import requests
from bs4 import BeautifulSoup


class PokemonInfo:
    def __init__(self, number):
        self.number = number
        self._soup = self._create_soup()
        self._info_general = self._info_general()
        self.name = self.get_name()

    def get_name(self):
        """
        Returns Pokémon species name given a Pokédex number.

        :return: Pokémon species name
        """
        p = self._info_general
        table = p.table
        row = table.tbody.contents[2]
        return row.contents[3].text

    def _info_general(self):
        """
        Returns BeautifulSoup instance of containing general Pokémon info.

        :return: BeautifulSoup instance containing general Pokémon info
        """
        table = self._soup.body.find_all('table')[1]
        row = table.tbody.contents[2]
        data = row.contents[3]
        div = data.font.contents[2].div
        return div.p

    def _create_soup(self):
        """
        Returns BeautifulSoup instance of the parsed Pokédex page.

        :return: BeautifulSoup instance containing parsed Pokédex page
        """
        url = self._number_to_url()
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html5lib')

    def _number_to_url(self):
        """
        Returns the url of the Pokédex page for a given Pokédex number.

        :return: url
        """
        num_string = self._dex_number()
        return "https://serebii.net/pokedex-sm/" + num_string + ".shtml"

    def _dex_number(self):
        """
        Converts an integer number to a 3-digit string.

        :return: dex number in the form of a 3-digit string
        """
        number = str(self.number)
        while len(number) < 3:
            number = '0' + number
        return number
