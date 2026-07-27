# armor.py 

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a value between 0 and the value set by self.max_block. 
        '''
        import random
        return random.randint(0, self.max_block)
    