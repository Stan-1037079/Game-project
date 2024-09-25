from typing import List, Tuple
from fire_type import fire_benefits
from grass_type import grass_benefits
from water_type import water_benefits

class Pokemon():

    def __init__(self, name: str, types: str, level: int, health: int, attack: int, defense: int, moves: List[Tuple[str, int]]) -> None:
        self.name = name
        self.type = types
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense
        self.moves = moves
        self.fight_status: bool = False
        self.alive: bool = True
    
    def type_benefits(self):
        if self.type == 'Fire':
            return fire_benefits()
        elif self.type == 'Grass':
            return grass_benefits()
        elif self.type == 'Water':
            return water_benefits()