from random import choice

class Pound:

    def __init__(self, rare = False):

        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1
        self.color = 'gold'
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True

    def rust(self):
        self.color = 'greenish'

    def clean(self):
        self.color = 'gold'

    def flip(self):
        options = [True,False]
        self.heads = choice(options)
        print(self.heads)

    def __del__(self):
        print('Coin Spent!')

coin1 = Pound()
coin1.flip()
