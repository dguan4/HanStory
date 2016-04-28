"""
Weapon class for the RPG Game
Separate from the item class
"""

from constants import WEAPONS


class Weapon:

    def __init__(self, name):
        """
        Initialize the weapon based on the item given
        :param name: Name of the weapon
        :return:
        """
        self.name = name
        self.mt = WEAPONS[name]
