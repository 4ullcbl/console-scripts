from world.gen.generator import Generator

import random
from block.blocks import STONE
from block.blocks import AIR
from block.blocks import COAL
from block.blocks import GOLD
from block.blocks import CUPRUM

class FastGen(Generator):
    def __init__(self, width, height, seed=random.randint(0, 9999999)):
        self.height = height
        self.width = width
        self.seed = seed
    
    def gen(self) -> list:
        result = []

        for i in range(self.width * self.height):
            chance = random.randint(1, 100)
            
            if i > 0 and result[i-1] == AIR and chance >= 25:
                result.append(AIR)
                continue

            if chance <= 80:
                result.append(STONE)
            elif 99 >= chance >= 90:
                result.append(AIR)
            elif chance >= 99:
                result.append(GOLD)
            elif 83 == chance and i > 0 and result[i-1] == STONE:
                result.append(COAL)
            elif random.randint(1, 100) == 1:
                result.append(CUPRUM)
            else:
                result.append(STONE)

        return result
