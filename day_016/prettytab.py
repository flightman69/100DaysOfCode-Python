from prettytable import PrettyTable

table = PrettyTable()


pokemons = {
        "Pikachu" : "Electric",
        "Squirtle": "Water",
        "Charmander": "Fire",
        }
pokemon_name = list(pokemons.keys())
pokemon_type = list(pokemons.values())
table.add_column("Pokemon Name",pokemon_name)
table.add_column("Pokemon Type",pokemon_type)
table.align = "l"

print(table)
