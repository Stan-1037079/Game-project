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

def switch_pokemon(current_pokemon, available_pokemon):
    """Laat de speler wisselen van Pokémon."""
    print("Choose a new Pokemon to switch to:")
    for index, pokemon in enumerate(available_pokemon):
        # Zorg ervoor dat de speler niet de huidige Pokémon opnieuw kan kiezen of een al verslagen Pokémon kan kiezen
        if pokemon != current_pokemon and pokemon.alive:
            print(f"{index + 1}. {pokemon.name} (Type: {pokemon.type}, HP: {pokemon.health})")
    
    choice = int(input("Select a number to switch to: ")) - 1
    new_pokemon = available_pokemon[choice]
    
    print(f"You switched to {new_pokemon.name}!")
    return new_pokemon

def battle(player_pokemon, opponent_pokemon, player_team):
    """Turn based battle with the option to switch Pokemon."""
    print(f"\n{player_pokemon.name} (Player) vs {opponent_pokemon.name} (Opponent)")
    
    while player_pokemon.alive and opponent_pokemon.alive:
        # Player's turn
        print("\nYour turn!")
        print(f"Your Pokemon: {player_pokemon.name} (HP: {player_pokemon.health})")
        print(f"Opponent: {opponent_pokemon.name} (HP: {opponent_pokemon.health})")
        
        print("Choose an action:")
        print("1. Attack")
        print("2. Switch Pokemon")
        
        action_choice = int(input("Choose an action (1-2): "))
        
        if action_choice == 1:
            # Player chooses a move
            print("Choose a move:")
            for index, move in enumerate(player_pokemon.moves):
                print(f"{index + 1}. {move[0]} (Type: {move[2]}, Power: {move[1]})")
            
            move_choice = int(input("Choose a move (1-2): ")) - 1
            player_pokemon.attack_opponent(move_choice, opponent_pokemon)
        
        elif action_choice == 2:
            # Player switches Pokémon
            player_pokemon = switch_pokemon(player_pokemon, player_team)

        # Check if opponent is defeated
        if not opponent_pokemon.alive:
            print(f"\n{opponent_pokemon.name} has been defeated!")
            break

        # Opponent's turn
        print("\nThe opponent attacks!")
        opponent_move_choice = random.randint(0, len(opponent_pokemon.moves) - 1)
        opponent_pokemon.attack_opponent(opponent_move_choice, player_pokemon)

        # Check if player is defeated
        if not player_pokemon.alive:
            print(f"\n{player_pokemon.name} is defeated!")
            break

