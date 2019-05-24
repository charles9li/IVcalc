import unittest
from webscrape.webscrape_utils import PokemonInfo


class TestPokemonInfo(unittest.TestCase):

    def test_name(self):
        pokemon = PokemonInfo(1)
        self.assertEqual("Bulbasaur", pokemon.name, "Should be Bulbasaur")
        pokemon = PokemonInfo(3)
        self.assertEqual("Venusaur", pokemon.name, "Should be Venusaur")

    def test_base_states(self):
        pokemon = PokemonInfo(1)
        self.assertEqual([45, 49, 49, 65, 65, 45], pokemon.base_stats)
        pokemon = PokemonInfo(3)
        self.assertEqual([80, 82, 83, 100, 100, 80], pokemon.base_stats)


if __name__ == '__main__':
    unittest.main()