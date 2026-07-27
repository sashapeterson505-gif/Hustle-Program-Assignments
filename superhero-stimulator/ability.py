# ability.py 

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):  #random attack damage between 0 and max_damage
        ''' Return a value between 0 and the value set by self.max_damage. 
        '''
        import random
        return random.randint(0, self.max_damage) #needed help so ai helped a bit with this one, but I understand it now
    
    