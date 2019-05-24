import requests
from bs4 import BeautifulSoup


class PokemonInfo:
    """
    Contains information about a Pokemon including species name, Pokedex
    number, evolutions, and base stats.
    """

    def __init__(self, dex_num):
        """
        Constructor for PokemonInfo class. Takes in a Pokedex number and
        scrapes a website to get information.

        :param dex_num: Pokedex number
        """
        self.dex_num = dex_num
        self._dex_num_str = self._dex_num_str()
        self._soup = self._create_soup()
        self.name = self._get_name()
        self.base_stats = self._get_base_stats()

    #################
    # SOUP CREATION #
    #################

    def _create_soup(self):
        """
        Returns BeautifulSoup instance of the parsed Pokedex page.

        :return: BeautifulSoup instance containing parsed Pokedex page
        """
        url = self._number_to_url()
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html5lib')

    def _number_to_url(self):
        """
        Returns the url of the Pokedex page for a given Pokedex number.

        :return: url
        """
        return "https://serebii.net/pokedex-sm/" + self._dex_num_str + ".shtml"

    def _dex_num_str(self):
        """
        Converts an integer number to a 3-digit string.

        :return: dex number in the form of a 3-digit string
        """
        number = str(self.dex_num)
        while len(number) < 3:
            number = '0' + number
        return number

    ########
    # NAME #
    ########

    def _get_name(self):
        """
        Returns the name of the Pokemon.

        :return: name of Pokemon
        """
        tag = self._name_tag()
        return tag.parent.next_sibling.next_sibling.contents[3].text

    def _name_tag(self):
        """
        Returns the tag that has the "Name" text.

        :return: tag with "Name" text
        """
        return self._soup.find(self._has_name_text)

    ##############
    # BASE STATS #
    ##############

    def _get_base_stats(self):
        """
        Returns list of base stats.

        :return: list of base stats
        """
        tag = self._stats_tag()
        tag = tag.parent.parent.parent.contents[3]
        return [int(tag.contents[i].text) for i in range(2, 14, 2)]

    def _stats_tag(self):
        """
        Returns the tag that has the "Stats" text.

        :return: tag with "Stats" text
        """
        return self._soup.find(self._has_stats_text)

    ###########
    # FILTERS #
    ###########

    @staticmethod
    def _has_name_text(tag):
        """
        Filter used to find "Name" tag.

        :param tag: node in soup
        :return: True if tag has "Name" text
        """
        try:
            return tag.text == "Name" and tag['class'][0] == "fooevo"
        except AttributeError:
            return False

    @staticmethod
    def _has_stats_text(tag):
        """
        Filter used to find "Stats" tag.

        :param tag: node in soup
        :return: True if tag has "Stats" text
        """
        try:
            return tag.text == "Stats" and tag.name == "b"
        except AttributeError:
            return False

    ##############
    # PRINT INFO #
    ##############

    @staticmethod
    def print_info_header():
        """
        Prints header for output info.
        """
        output = "Dex# Name" + " "*13
        output = output + "HP ATK DEF SPA SPD SPE"
        print(output)
        print("="*len(output))

    def print_info(self):
        """
        Prints Pokemon info.
        """
        output = self._dex_num_str + " "*2
        output = output + self.name + " "*(15 - len(self.name))
        for i in range(0, 6):
            stat_str = str(self.base_stats[i])
            output = output + " "*(4 - len(stat_str)) + stat_str
        print(output)
