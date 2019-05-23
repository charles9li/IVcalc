import unittest
from database.webscrape_utils import PokemonInfo


class TestPokemonInfo(unittest.TestCase):

    def test_name(self):
        pokemon = PokemonInfo(1)
        self.assertEqual("Bulbasaur", pokemon.name, "Should be Bulbasaur")


if __name__ == '__main__':
    unittest.main()