from pokemon import Pokemon

stroomrat = Pokemon('Stroomrat', 'Electric', 5, 15, 3, 3, [('Thunder Shock', 1, 'Electric'), ('Quick Attack', 1,'Normal')])
vuurhond = Pokemon('Vuurhond', 'Fire', 5, 15, 3, 3, [('Ember', 1, 'Fire'), ('Quick Attack', 1,'Normal')])
waterkip = Pokemon('Waterkip', 'Water', 5, 15, 3, 3, [('Water Gun', 1, 'Water'), ('Quick Attack', 1,'Normal')])
grasvarken = Pokemon('Grasvarken', 'Grass', 5, 15, 3, 3, [('Vine Whip', 1, 'Grass'), ('Quick Attack', 1,'Normal')])
normiekat = Pokemon('Normiekat', 'Normal', 5, 15, 3, 3, [('Tackle', 1, 'Normal'), ('Quick Attack', 1,'Normal')])
graafmol = Pokemon('Graafmol', 'Ground', 5, 15, 3, 3, [('Dig', 1, 'Ground'), ('Quick Attack', 1,'Normal')])

print(f'{stroomrat.name, stroomrat.type, stroomrat.level, stroomrat.health, stroomrat.attack, stroomrat.defense, stroomrat.moves}')