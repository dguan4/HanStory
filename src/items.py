"""
Item class for the RPG
Determines the type of item it is and everything
"""

from constants import ITEMS

class Item:

    def __init__(self, name):
        """
        Sets the type of the items and
        :param name: name of the item
        :return:
        """
        self.name = name
        self.usage = ITEMS[self.name][0]
        self.amount = ITEMS[self.name][1]
