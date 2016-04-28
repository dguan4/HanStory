"""
Map Object for the Python RPG
"""
from constants import *


class Map:

    def __init__(self):
        #simple binary system to have blocks, 0 being
        self.map = [[0]*16 for n in range(20)]
        self.player = None
        self.player_loc = (0, 0)
        self.treasure_loc = (0, 0)
        self.monster_loc = (0, 0)

    def set_player_location(self, location):
        """
        Sets player location to be a certain x,y
        :param location: location of the player
        :return: true if an item is removed
        """
        self.player_loc = location
        if self.map[location[0]//TILE_SIZE][location[1]//TILE_SIZE] == 1:
            self.remove_item(location)
            return True
        if self.map[location[0]//TILE_SIZE][location[1]//TILE_SIZE] == 2:
            self.remove_monster(location)
            return 2
        return False

    def set_monster_location(self, location):
        """
        Sets the monster location to be a certain x,y
        :param location: location of the monster
        :return: true if set, false if something else is there
        """
        if self.map[location[0]//TILE_SIZE][location[1]//TILE_SIZE] == 1:
            return False
        self.monster_loc = location
        self.add_monster(location)
        return True

    def add_item(self, location):
        """
        Adds an item to a location
        :param location: location to add the item
        :return:
        """
        if self.map[location[0]][location[1]] == 2:
            return False
        self.map[location[0]][location[1]] = 1
        return True

    def remove_item(self, location):
        """
        TODO: update positions and remove item from a location
        :param location: location to check in the map
        :return:
        """
        self.map[location[0]//TILE_SIZE][location[1]//TILE_SIZE] = 0

    def add_monster(self, location):
        """
        Adds a monster to a location
        :param location: location to add monster
        :return:
        """
        self.map[location[0]//TILE_SIZE][location[1]//TILE_SIZE] = 2

    def remove_monster(self, location):
        """
        Removes a monster from a location
        :param location: location to remove
        :return:
        """
        self.map[location[0]//TILE_SIZE][location[1]//TILE_SIZE] = 0

