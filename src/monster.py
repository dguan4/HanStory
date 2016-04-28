"""
Monster class
"""

import random
from constants import *


class Monster:

    def __init__(self):
        """
        Initializes the monster's stats
        :return:
        """
        self.level = random.randint(1, 4)
        self.max_hp = random.randint(29, 34)
        self.hp = self.max_hp
        self.stats = {'str': random.randint(30, 37), 'mag': 1, 'skill': random.randint(9, 12),
                      'spd': random.randint(6, 9), 'def': random.randint(5, 9), 'lck': 12, 'res': 4}
        self.inventory = random.choice(list(ITEMS))
        self.x_y, self.loc = self.set_location()

    def attack(self, defense):
        """
        Getter to return the damage that would be dealt
        :return:
        """
        return self.stats['str'] - defense

    def receive_damage(self, damage):
        """
        Receives damage from player
        :return:
        """
        dmg = max(0, damage - self.stats['def'])
        self.hp -= dmg

    def set_location(self):
        """
        Sets a new location for the monster
        :return:
        """
        rand_col = random.randint(0, COLUMN-1)
        rand_row = random.randint(0, ROW-1)
        x_y = (rand_row, rand_col)
        loc = (rand_row*TILE_SIZE, rand_col*TILE_SIZE)
        return x_y, loc
