import requests
from bs4 import BeautifulSoup


class PokemonInfo:
    """
    Contains information about a Pokémon including species name, Pokédex
    number, evolutions, and base stats.
    """

    def __init__(self, number):
        """
        Constructor for PokemonInfo class. Takes in a Pokédex number and
        scrapes a website to get information.

        :param number: Pokédex number
        """
        self.number = number
        self.number_string = self._dex_number()
        self._soup = self._create_soup()
        self._info_full = self._info_full()
        self._info_general = self._info_general()
        self._info_moves = self._info_moves()
        self._info_stats = self._info_stats()
        self.name = self._get_name()
        self.base_stats = self._base_stats()

    def _get_name(self):
        """
        Returns Pokémon species name given a Pokédex number.

        :return: Pokémon species name
        """
        p = self._info_general
        table = p.table
        row = table.tbody.contents[2]
        name = row.contents[3].text
        return name

    def _info_full(self):
        """
        Returns BeautifulSoup instance of containing full Pokémon info.

        :return: BeautifulSoup instance containing general Pokémon info
        """
        table = self._soup.body.find_all('table')[1]
        row = table.tbody.contents[2]
        data = row.contents[3]
        return data.font.contents[2].div

    def _info_general(self):
        """
        Returns BeautifulSoup instance of containing general Pokémon info.

        :return: BeautifulSoup instance containing general Pokémon info
        """
        return self._info_full.p

    def _info_moves(self):
        """
        Returns BeautifulSoup instance containing Pokémon move and stat info.

        :return: BeautifulSoup instance containing move and stat info
        """
        return self._info_full.div

    def _info_stats(self):
        """
        Returns BeautifulSoup instance of containing Pokémon base state info.

        :return: BeautifulSoup instance containing base stat info
        """
        return self._info_moves.ul.li.contents[-1].contents[-1].tbody.contents[3]

    def _base_stats(self):
        """
        Takes stats info nad returns an list of base stats.

        :return: list of base stats of Pokémon
        """
        return [int(self._info_stats.contents[i].contents[0]) for i in range(2, 14, 2)]

    def _create_soup(self):
        """
        Returns BeautifulSoup instance of the parsed Pokédex page.

        :return: BeautifulSoup instance containing parsed Pokédex page
        """
        url = self._number_to_url()
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html5lib')

    def _dex_number(self):
        """
        Converts an integer number to a 3-digit string.

        :return: dex number in the form of a 3-digit string
        """
        number = str(self.number)
        while len(number) < 3:
            number = '0' + number
        return number

    def _number_to_url(self):
        """
        Returns the url of the Pokédex page for a given Pokédex number.

        :return: url
        """
        return "https://serebii.net/pokedex-sm/" + self.number_string + ".shtml"
