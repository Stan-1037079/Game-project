from pokemon_battle import choose_pokemon, opponent_choice, battle
from pokemon_list import get_pokemon_list

# Get a list of available Pokemon
available_pokemon = get_pokemon_list()

# Player chooses a Pokemon
player_pokemon = choose_pokemon(available_pokemon)

# Opponent chooses a Pokemon
opponent_pokemon = opponent_choice(available_pokemon)

# Starts the battle
battle(player_pokemon, opponent_pokemon)
