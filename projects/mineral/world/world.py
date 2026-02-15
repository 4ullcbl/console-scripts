import random

from world.gen.generator import Generator
from player.player import Player
from block.blocks import AIR

class World:

    def __init__(self, player: Player, width, height, objects=[], seed=random.randint(0, 9999999)):
        self.width = width
        self.height = height
        self.seed = seed
        self.player = player
        self.objects = objects

    def generate(self, generator: Generator):
        self.objects = generator.gen()

    def set_player_loc(self, loc):
        self.player.set_loc(loc)
    
    def get_block(self, loc) -> str:
        return self.objects[loc]

    def break_block(self, loc):
        try:
            block = self.objects[loc]

            if block == AIR:
                return
        
            self.player.add_item(block)

            self.objects[loc] = AIR
        except IndexError:
            return
    def print(self):
         
        for i in range(len(self.objects)):
            if i % self.width == 0:
                print()
            
            if i == self.player.loc:
                print(self.player.char, end="")
            else:
                print(self.objects[i], end ="")

