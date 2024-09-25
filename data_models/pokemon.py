from typing import List, Tuple
from fire_type import fire_benefits
from grass_type import grass_benefits
from water_type import water_benefits
from normal_type import normal_benefits
from electric_type import electric_benefits
from ground_type import ground_benefits

class Pokemon():
    #Base stats for a pokemon
    def __init__(self, name: str, types: str, level: int, health: int, attack: int, defense: int, moves: List[Tuple[str, int, str]]) -> None:
        self.name = name
        self.type = types
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.moves = moves
        self.fight_status: bool = False
        self.alive: bool = True
        self.type_benefits = self.type_benefits()
    
    # All types and their benefits
    def type_benefits(self):
        if self.type == 'Fire':
            return fire_benefits()
        elif self.type == 'Grass':
            return grass_benefits()
        elif self.type == 'Water':
            return water_benefits()
        elif self.type == 'Normal':
            return normal_benefits()
        elif self.type == 'Electric':
            return electric_benefits()
        elif self.type == 'Ground':
            return ground_benefits()
        else:
            return {'strong_against': None, 'weak_against': None, 'resists': None, 'immune': None}
    
    def calculate_damage(self, opponent) -> float:
        base_damage = self.attack - opponent.defense

        # Checks if pokemon is immune to the type of the opponent
        if opponent.type_benefits.get('immune') == self.type:
            print(f"{self.name} it doesn't affect the opponent {opponent.name}")
            return 0  # No damage calculated

        # Checks if pokemon is Electric and opponent is Ground
        if self.type == 'Electric' and opponent.type == 'Ground':
            print(f"{self.name} it doesn't affect the opponent {opponent.name}!")
            return 0  # No damage calculated
        
        if self.type_benefits['strong_against'] and opponent.type in self.type_benefits['strong_against']:
            return base_damage * 2  # Attack bonus x2 damage if own type is strong against opponent
        elif self.type_benefits.get('weak_against') and opponent.type in self.type_benefits['weak_against']:
            return base_damage * 0.5  # Attack penalty x0.5 damage if own type is weak against opponent
        elif opponent.type_benefits.get('resists') == self.type:
            return base_damage * 0.5  # Defense bonus x0.5 damage if opponent resists your type
        else:
            return base_damage 