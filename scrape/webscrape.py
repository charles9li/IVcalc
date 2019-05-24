from scrape.webscrape_utils import PokemonInfo
import sqlite3


# Create connection
conn = sqlite3.connect('c:/users/charles/ivcalc/database/pokemon.db')
c = conn.cursor()

# Delete previous table
c.execute("DROP TABLE [IF EXISTS] data")

# Create table
c.execute("CREATE TABLE IF NOT EXISTS data "
          "(number, name, hp, atk, def, spa, spd, spe)")

# Insert pokemon data into table
PokemonInfo.print_info_header()
for dex_num in range(1, 808):
    pokemon = PokemonInfo(dex_num)
    c.execute("INSERT INTO data VALUES "
              "(?, ?, ?, ?, ?, ?, ?, ?)",
              (pokemon.dex_num, pokemon.name,
               pokemon.base_stats[0], pokemon.base_stats[1],
               pokemon.base_stats[2], pokemon.base_stats[3],
               pokemon.base_stats[4], pokemon.base_stats[5]))
    pokemon.print_info()

# Save (commit) the changes and close connection
conn.commit()
conn.close()
