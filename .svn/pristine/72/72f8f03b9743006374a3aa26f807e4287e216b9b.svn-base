"""
Player class for the RPG game
"""

from constants import *
from weapon import Weapon
from items import Item
from inventory import Inventory

class Player:

    def __init__(self):
        """
        Initializing our player with his initial stats
        These are what I feel players should start out with
        Hans' stats vary within the game
        :return:
        """
        self.level = 1
        self.stats = {'str': 12, 'mag': 1, 'skill': 13, 'spd': 13, 'def': 15, 'lck': 12, 'res': 4}
        self.growths = {'hp': 0.8, 'str': 0.6, 'mag': 0.2, 'skill': 0.7, 'spd': 0.7, 'def': 0.6, 'luk': 0.3, 'res': 0.3}
        self.hp = 30
        self.max_hp = 30
        self.name = "Hans"
        self.inventory = Inventory()
        self.equipped = self.inventory.get_specific_item("Steel Axe")
        self.loc = (1, 1)

    def receive_damage(self, damage):
        """
        Receiving damage to the player
        :param damage: total damage being received
        :return:
        """
        dmg = max(0, damage - self.stats['def'])
        self.hp = max(0, self.hp-dmg)

    def attack(self, defense):
        """
        Returns the damage dealt to an enemy
        If the player is not equipped with anything, simply return 0
        :param def: opposing enemy's def
        :return: damage dealt
        """
        if self.equipped:
            return self.stats['str'] + self.equipped.mt - defense
        return 0

    def equip_item(self, item):
        """
        Equips an item. Has to be a weapon
        :param item: weapon to equip
        :return:
        """
        if isinstance(item, Weapon) and item.name in self.inventory.get_items():
            self.equipped = item

    def add_to_inventory(self, item):
        """
        Adds an item to the inventory
        Following Fates, we only allow 5 item slots
        :param item: item to add to inventory
        :return:
        """
        return self.inventory.add_to_inventory(item)

    def remove_from_inventory(self, item):
        """
        Removes an item from an inventory
        TODO: find a good way to remove an item after using a healing item
        :param item: item to be removed
        :return:
        """
        if item.name in self.inventory.get_items():
            self.inventory.remove_from_inventory(item)

    def inc_max_hp(self, amount):
        """
        Increases the max hp, mostly from leveling up or items
        :param amount: amount to increase by
        :return:
        """
        self.max_hp += amount

    def use_item(self, item):
        """
        Usage of an item, must not be a weapon
        :param item:
        :return:
        """
        if item.name in self.inventory.get_items():
            if item.usage == "HEALING":
                self.hp = min(self.max_hp, self.hp+item.amount)
            if item.usage == "SERAPH":
                self.inc_max_hp(item.amount)

    def set_location(self, location):
        """
        Sets the location of the player
        :param location: location to set
        :return:
        """
        self.loc = location
