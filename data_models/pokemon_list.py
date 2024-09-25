from pokemon import Pokemon

stroomrat = Pokemon('Stroomrat', 'Electric', 5, 15, 3, 3, [('Thunder Shock', 1), ('Quick Attack', 1)])
vuurhond = Pokemon('Vuurhond', 'Fire', 5, 15, 3, 3, [('Ember', 1), ('Quick Attack', 1)])
waterkip = Pokemon('Waterkip', 'Water', 5, 15, 3, 3, [('Water Gun', 1), ('Quick Attack', 1)])
grasvarken = Pokemon('Grasvarken', 'Grass', 5, 15, 3, 3, [('Vine Whip', 1), ('Quick Attack', 1)])
normiekat = Pokemon('Normiekat', 'Normal', 5, 15, 3, 3, [('Tackle', 1), ('Quick Attack', 1)])
graafmol = Pokemon('Graafmol', 'Ground', 5, 15, 3, 3, [('Dig', 1), ('Quick Attack', 1)])

print(f'{stroomrat.name, stroomrat.type, stroomrat.level, stroomrat.health, stroomrat.attack, stroomrat.defense, stroomrat.moves}')