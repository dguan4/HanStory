"""
Tests for the Game
This simply tests the clases to make sure no edge cases are left out
Does not test gui cause I don't know how
"""

from unittest import TestCase
from player import Player
from items import Item
from inventory import Inventory
from weapon import Weapon
from monster import Monster
from combat import Combat

class TestGame(TestCase):

    def test_game(self):
        """
        Tests the player class to make sure functions work properly
        :return: true if everything passes
        """
        player = Player()
        self.assertIs(player.level, 1)
        self.assertEquals(player.stats, {'str': 12, 'mag': 1, 'skill': 13, 'spd': 13, 'def': 15, 'lck': 12, 'res': 4})
        self.assertEquals(player.growths, {'hp': 0.8, 'str': 0.6, 'mag': 0.2, 'skill': 0.7, 'spd': 0.7, 'def': 0.6, 'luk': 0.3, 'res': 0.3})
        self.assertIs(player.hp, 30)
        self.assertIs(player.max_hp, 30)
        self.assertIs(player.name,"Hans")
        self.assertIsInstance(player.equipped, Weapon)
        self.assertIsInstance(player.inventory, Inventory)

        player.receive_damage(5)
        #player health should be same
        self.assertIs(player.hp, 30)
        player.receive_damage(16)
        #player health should subtract 1
        self.assertIs(player.hp, 29)

        player.inc_max_hp(1)
        self.assertIs(player.max_hp, 31)

        #now test items
        weapon = Weapon("Steel Axe")
        self.assertIs(weapon.name, "Steel Axe")
        player.add_to_inventory(weapon)
        #item should be in inventory
        self.assertTrue(weapon.name in player.inventory.get_items())
        player.equip_item(weapon)
        #item should be equipped
        self.assertIs(player.equipped, weapon)

        #attack a random enemy with 5 defense
        att = player.attack(5)
        self.assertIs(att, 19)

        item = Item("Vulnerary")
        #remember we have 29 hp right now so this should just heal full
        player.use_item(item)
        self.assertIs(player.hp, 31)

        item = Item("Seraph Robe")
        player.add_to_inventory(item)
        player.use_item(item)
        self.assertIs(player.max_hp, 38)

        #testing remove inventory
        player.remove_from_inventory(item)
        self.assertFalse(item in player.inventory.get_items())

    def test_inventory(self):
        """
        Tests the inventory class to make sure everything works
        :return:
        """
        inventory = Inventory()
        list_of_items = list(inventory.inventory.keys())
        #test initializing

        self.assertTrue("Steel Axe" in list_of_items)
        self.assertTrue("Vulnerary" in list_of_items)

        #test get_items function
        self.assertEquals(inventory.get_items(), list_of_items)

        #test adding items
        item = Weapon("Silver Axe")
        inventory.add_to_inventory(item)
        list_of_items = inventory.get_items()
        self.assertTrue("Silver Axe" in list_of_items)
        item = Weapon("Iron Axe")
        inventory.add_to_inventory(item)
        item = Item("Seraph Robe")
        inventory.add_to_inventory(item)
        list_of_items = inventory.get_items()
        self.assertIs(len(list_of_items), 5)

        #test limit of inventory
        item = Item("Concoction")
        inventory.add_to_inventory(item)
        list_of_items = inventory.get_items()
        self.assertIs(len(list_of_items), 5)
        self.assertFalse("Concoction" in list_of_items)

        #test removing items
        item = Item("Seraph Robe")
        inventory.remove_from_inventory(item)
        list_of_items = inventory.get_items()
        self.assertFalse("Seraph Robe" in list_of_items)


