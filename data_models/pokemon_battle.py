import random
from pokemon_list import get_pokemon_list
from pokemon import Pokemon

def choose_pokemon(pokemon_list):
    """Let the player choose out of 6 Pokémon."""
    random_pokemon = random.sample(pokemon_list, 6)
    print("Choose your Pokemon:")
    for index, pokemon in enumerate(random_pokemon):
        print(f"{index + 1}. {pokemon.name} (Type: {pokemon.type}, HP: {pokemon.health}, Attack: {pokemon.attack}, Defense: {pokemon.defense})")

    choice = int(input("Select a number (1-6): ")) - 1
    return random_pokemon[choice]

def opponent_choice(pokemon_list):
    """Let the opponent choose out of 6 Pokémon"""
    random_pokemon = random.sample(pokemon_list, 6)
    print("Choose your Pokemon:")
    for index, pokemon in enumerate(random_pokemon):
        print(f"{index + 1}. {pokemon.name} (Type: {pokemon.type}, HP: {pokemon.health}, Attack: {pokemon.attack}, Defense: {pokemon.defense})")

    choice = int(input("Select a number (1-6): ")) - 1
    return random_pokemon[choice]

def battle(player_pokemon, opponent_pokemon):
    """Turn based battle."""
    print(f"\n{player_pokemon.name} (Player) vs {opponent_pokemon.name} (Opponent)")
    
    while player_pokemon.alive and opponent_pokemon.alive:
        # Player chooses a move
        print("\nYour turn!")
        print(f"Your Pokemon: {player_pokemon.name} (HP: {player_pokemon.health})")
        print(f"Opponent: {opponent_pokemon.name} (HP: {opponent_pokemon.health})")
        
        print("Choose a move:")
        for index, move in enumerate(player_pokemon.moves):
            print(f"{index + 1}. {move[0]} (Type: {move[2]}, Power: {move[1]})")
        
        move_choice = int(input("Choose a move (1-2): ")) - 1
        player_pokemon.attack_opponent(move_choice, opponent_pokemon)

        # Checks if opponent is defeated
        if not opponent_pokemon.alive:
            print(f"\n{opponent_pokemon.name} has been defeated! EZ win!")
            break

        # Opponent chooses a move
        print("\nThe opponent attacks!")
        opponent_move_choice = random.randint(0, len(opponent_pokemon.moves) - 1)
        opponent_pokemon.attack_opponent(opponent_move_choice, player_pokemon)

        # Checks if player is defeated
        if not player_pokemon.alive:
            print(f"\n{player_pokemon.name} is defeated! you lose noob!")
            break
