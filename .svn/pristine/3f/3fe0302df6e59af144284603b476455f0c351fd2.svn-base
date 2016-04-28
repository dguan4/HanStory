"""
Treasure class for the Game
Creates all treasures on the map
"""
from constants import *
import random
from weapon import Weapon
from items import Item

class Treasure:

    def __init__(self):
        """
        Initializes the item located in the treasure randomly
        :return:
        """
        list_items = list(ITEMS.keys())
        for i in list(WEAPONS.keys()):
            list_items.append(i)
        self.name = random.choice(list_items)
        if self.name in WEAPONS:
            self.item = Weapon(self.name)
        else:
            self.item = Item(self.name)
        rand_col = random.randint(0, COLUMN-1)
        rand_row = random.randint(0, ROW-1)
        self.x_y = (rand_row, rand_col)
        self.loc = (rand_row*TILE_SIZE, rand_col*TILE_SIZE)
