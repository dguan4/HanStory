"""
Python PRG Game made with PyGame
"""

from constants import *
from map import Map
from view import View
from player import Player
from items import Item
from treasure import Treasure
from weapon import Weapon
from pygame.locals import *
from monster import Monster
from combat import Combat
from button import Button
import pickle
import time
import pygame
import sys


class Game:

    def __init__(self):
        """
        Sets up a game gui with the player and starts it
        :return:
        """
        pygame.init()
        self.view = View()
        self.map = Map()
        self.map.player = Player()
        self.map.player_loc = (1*TILE_SIZE, 1*TILE_SIZE)
        self.player = self.map.player
        self.player.set_location(self.map.player_loc)
        #self.time = pygame.time.Clock()
        self.map.set_player_location(self.map.player_loc)
        self.treasure = Treasure()
        self.inventory_button = Button("Inventory", 480, 0, 20, 20)
        self.save_button = Button("Save", 590, 0, 20, 20)
        self.load_button = Button("Load", 590, 50, 20, 20)
        self.view.draw_layers(self.map, self.treasure, self.map.player.inventory, self.inventory_button, self.save_button, self.load_button)
        self.monster = Monster()
        self.map.monster_loc = self.monster.loc
        while self.map.set_monster_location(self.monster.loc) is False:
            self.monster.set_location()
        self.map.treasure_loc = self.treasure.x_y
        while self.map.add_item(self.treasure.x_y) is False:
            self.treasure = Treasure()

    def move_player(self, direction):
        """
        Moves the player in a certain direction given a keypress
        :param direction: direction to move in
        :return:
        """
        oldx, oldy = self.map.player_loc
        x, y = oldx + direction[0], oldy + direction[1]
        x_limit = (ROW-1) * TILE_SIZE
        y_limit = (COLUMN-1) * TILE_SIZE
        #don't do anything if the location is too much
        if x > x_limit or x < 0 or y > y_limit or y < 0:
            return
        ret_move_player = self.map.set_player_location((x, y))
        self.player.set_location((x, y))
        if ret_move_player is True:
            self.map.player.add_to_inventory(self.treasure.item)
            self.treasure = Treasure()
            self.map.treasure_loc = self.treasure.x_y
            print(self.map.player.inventory.get_items())
            self.map.add_item(self.treasure.x_y)
        elif ret_move_player is 2:
            print("COMBAT")
            hp = Combat(self.map.player, self.monster, self.view).init_combat()
            print(hp)
            if hp[0] <= 0:
                self.end_game()
                return False
                #self.quit()
            else:
                self.map.player.hp = hp[0]
            self.monster = Monster()
            while self.map.set_monster_location(self.monster.loc) is False:
                self.monster.set_location()
            self.map.monster_loc = self.monster.loc
            self.map.add_monster(self.monster.loc)

    def get_inventory(self):
        """
        Gets the inventory. This is called when the button is clicked
        :return:
        """
        self.view.draw_inventory(self.player.inventory)
        pygame.display.flip()

    def refresh(self, inventory):
        """
        Refreshes the current view
        :param inventory: inventory to include
        :return:
        """
        self.view.draw_player(self.map.player_loc)
        self.view.draw_monster(self.map.monster_loc)
        self.view.draw_layers(self.map, self.treasure, inventory, self.inventory_button, self.save_button, self.load_button)

    def end_game(self):
        """
        Returns a game over screen
        :return:
        """
        self.view.draw_end_game()

    def quit(self):
        """
        Simple end game thing
        :return:
        """
        sys.exit()

#Game()