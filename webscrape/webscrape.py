from database.webscrape_utils import PokemonInfo
import sqlite3


# Create connection
conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

# Delete previous table
c.execute("DROP TABLE [IF EXISTS] data")

# Create table
c.execute("CREATE TABLE IF NOT EXISTS data "
          "(number, name, hp, atk, def, spa, spd, spe)")

# Insert pokemon data into table
for dex_num in range(1, 808):
    pokemon = PokemonInfo(dex_num)
    c.execute("INSERT INTO data VALUES "
              "(?, ?, ?, ?, ?, ?, ?, ?)",
              (pokemon.dex_num, pokemon.name,
               pokemon.base_stats[0], pokemon.base_stats[1],
               pokemon.base_stats[2], pokemon.base_stats[3],
               pokemon.base_stats[4], pokemon.base_stats[5]))
    print(pokemon._dex_num_str + " " + pokemon.name + " "*(15 - len(pokemon.name)) + str(pokemon.base_stats))

# Save (commit) the changes and close connection
conn.commit()
conn.close()
