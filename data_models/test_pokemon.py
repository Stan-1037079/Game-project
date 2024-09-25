from pokemon import Pokemon

test = Pokemon('test', 'Fire', 5, 15, 3, 3, [('test move ', 1)])

print(f'{test.name, test.type, test.level, test.health, test.attack, test.defense, test.moves}')