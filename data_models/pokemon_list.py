from pokemon import Pokemon

def get_pokemon_list():
    stroomrat = Pokemon('Stroomrat', 'Electric', 5, 20, 4, 2, [('Thunder Shock', 2, 'Electric'), ('Quick Attack', 1,'Normal')])
    vuurhond = Pokemon('Vuurhond', 'Fire', 5, 20, 4, 2, [('Ember', 2, 'Fire'), ('Quick Attack', 1,'Normal')])
    waterkip = Pokemon('Waterkip', 'Water', 5, 20, 4, 2, [('Water Gun', 2, 'Water'), ('Quick Attack', 1,'Normal')])
    grasvarken = Pokemon('Grasvarken', 'Grass', 5, 20, 4, 2, [('Vine Whip', 2, 'Grass'), ('Quick Attack', 1,'Normal')])
    normiekat = Pokemon('Normiekat', 'Normal', 5, 20, 4, 2, [('Tackle', 1, 'Normal'), ('Quick Attack', 1,'Normal')])
    graafmol = Pokemon('Graafmol', 'Ground', 5, 20, 4, 2, [('Dig', 2, 'Ground'), ('Quick Attack', 1,'Normal')])

    return [stroomrat, vuurhond, waterkip, grasvarken, normiekat, graafmol]

        #self.name = name
        #self.type = types
        #self.level = level
        #self.health = health
        #self.attack = attack
        #self.defense = defense
        #self.moves = moves
#print(f'{stroomrat.name, stroomrat.type, stroomrat.level, stroomrat.health, stroomrat.attack, stroomrat.defense, stroomrat.moves}')