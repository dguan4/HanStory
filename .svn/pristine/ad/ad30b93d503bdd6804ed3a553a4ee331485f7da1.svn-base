"""
Inventory Class for the RPG Game
"""

from weapon import Weapon
from items import Item
from constants import *


class Inventory:

    def __init__(self):
        """
        Sets up an initial inventory. Each player should have a Steel Axe and a Vulnerary to start
        :return:
        """
        self.inventory = {"Steel Axe": Weapon("Steel Axe"), "Vulnerary": Item("Vulnerary")}

    def get_items(self):
        """
        Returns the list of items currently in the inventory
        :return:
        """
        return list(self.inventory.keys())

    def add_to_inventory(self, item):
        """
        Adds an item to the inventory
        :param item: item to be added
        :return:
        """
        if len(self.inventory) < 5:
            self.inventory[item.name] = item
            return True
        else:
            return False

    def remove_from_inventory(self, item):
        """
        Removes an item from the inventory
        :param item: item to be deleted
        :return:
        """
        del self.inventory[item.name]

    def get_specific_item(self, item):
        """
        Gets the item object with the name we want
        :param item: item to get
        :return:
        """
        return self.inventory[item]

