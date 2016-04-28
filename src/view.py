"""
View class for the game
Supposedly it's easier to have a separate view class
Go figure huh? :)
"""

from constants import *
import pygame

class View:

    def __init__(self):
        """
        Initializing the views and everything
        TODO: get inventory to display
        :return:
        """
        pygame.init()
        self.screen = pygame.display.set_mode((620, 480))
        self.font = pygame.font.SysFont(None, 32)
        self.small_font = pygame.font.SysFont(None, 16)
        self.background = pygame.image.load('../assets/set1_background.png')
        self.player_blit = pygame.image.load('../assets/playerBlue_stand.png')
        self.treasure = pygame.image.load('../assets/greenGem.png')
        self.key = pygame.image.load('../assets/keyGreen.png')
        self.tiles = pygame.image.load('../assets/tileBrown_09.png')
        self.monster_blit = pygame.image.load('../assets/enemyFloating_1.png')
        self.combat_blit = pygame.image.load('../assets/set2_background.png')
        self.screen.blit(self.background, (0, 0))
        self.inventory = self.small_font.render("Inventory", True, WHITE, BLACK)
        #self.display_alert("Welcome to Hans' World")

    def draw_player(self, location):
        """
        Draws the player at a specific location
        :param location: location of the player
        :return:
        """
        self.screen.blit(self.player_blit, location)

    def display_alert(self, alert, color=WHITE):
        """
        Displays an alert at the top
        :param alert: alert to render
        :param color: color of the alert (white)
        :return:
        """
        alert = self.font.render(alert, True, color, BLACK)
        self.screen.blit(alert, (0, 480))

    def draw_background(self):
        """
        Draws the background
        :return:
        """
        self.screen.blit(self.background, (0, 0))

    def draw_treasure(self, location):
        """
        Draws a treasure at the location
        :param location: location of the treasure
        :return:
        """
        self.screen.blit(self.treasure, location)

    def draw_inventory(self, inventory):
        """
        Draws the inventory on the screen
        :param inventory: inventory to draw
        :return:
        """
        self.screen.blit(self.inventory, (480, 0))
        for i in range(len(inventory.get_items())):
            display = self.small_font.render(inventory.get_items()[i], True, WHITE, BLACK)
            self.screen.blit(display, (480, TILE_SIZE//2*(i+1)))

    def draw_health(self, hp, location):
        """
        Draws the player's health
        :param hp: hp to put
        :param location: location to put hp
        :return:
        """
        self.screen.blit(self.small_font.render("HP", True, WHITE, BLACK), location)
        self.screen.blit(self.small_font.render(str(hp), True, WHITE, BLACK), (location[0]+20, location[1]))

    def draw_monster(self, location):
        """
        Draws the monster at the location
        :param location: location to draw
        :return:
        """
        self.screen.blit(self.monster_blit, location)

    def draw_end_game(self):
        """
        Displays end game
        :return:
        """
        self.screen.blit(self.font.render("GAME OVER", True, WHITE, BLACK), (200, 300))
        pygame.display.flip()

    def draw_save_load(self, save, load):
        """
        Draws the save and load buttons
        :param save: save button
        :param load: load button
        :return:
        """
        self.draw_button(save)
        self.draw_button(load)

    def draw_layers(self, map, treasure, inventory, button, save, load):
        """
        Draw layers of the screen
        :param map map of the game
        :param treasure treasure location
        :param inventory of player
        :param button to draw
        :param save button to draw
        :param load button to draw
        :return:
        """
        self.draw_background()
        self.draw_player(map.player_loc)
        self.draw_health(map.player.hp, (50, 0))
        if treasure is not None:
            self.draw_treasure(treasure.loc)
        self.draw_monster(map.monster_loc)
        if inventory is not None:
            self.draw_inventory(inventory)
        self.draw_button(button)
        self.draw_save_load(save, load)
        pygame.display.flip()

    def draw_combat(self, player, monster, turn, hit):
        """
        Draws the combat system and displays the health bars
        :param player: player to draw
        :param monster: monster to draw
        :param turn: true if it is the player's turn
        :param hit: whether the action hit or not
        :return:
        """
        self.screen.blit(self.combat_blit, (0, 0))
        self.draw_player((200, 300))
        self.draw_monster((400, 300))
        if turn:
            self.screen.blit(self.font.render("ATTACK", True, WHITE, BLACK), (200, 100))
            if hit:
                self.screen.blit(self.font.render("HIT!", True, WHITE, BLACK), (400, 400))
            else:
                self.screen.blit(self.font.render("MISS!", True, WHITE, BLACK), (400, 400))
        else:
            self.screen.blit(self.font.render("ATTACK", True, WHITE, BLACK), (400, 100))
            if hit:
                self.screen.blit(self.font.render("HIT!", True, WHITE, BLACK), (200, 400))
            else:
                self.screen.blit(self.font.render("MISS!", True, WHITE, BLACK), (200, 400))
        self.draw_health(player.hp, (200, 200))
        self.draw_health(monster.hp, (400, 200))
        pygame.display.flip()

    def draw_button(self, button):
        """
        Draws the button at a certain location
        :param button: button to draw
        :return:
        """
        self.screen.blit(self.small_font.render(button.text, True, WHITE, BLACK),
                         pygame.Rect(button.x, button.y, button.width, button.height))
