"""
Simple Game loop function
"""

from game import Game
from pygame.locals import *
from constants import *
from view import View
import pygame
import pickle
import sys
import time

class GameLoop:
    
    def __init__(self):
        """
        Initializes the game loop
        :return:
        """
        self.game = Game()
        self.time = pygame.time.Clock()
        
    def run(self):
        """
        Runs the game loop
        :return:
        """
        x, y = 0, 0
        button_clicked = False
        while 1:
            self.time.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                #two types of events, prevents duplicate keys
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit(0)
                    if event.key == K_LEFT:
                        x = -TILE_SIZE
                        y = 0
                    if event.key == K_RIGHT:
                        x = TILE_SIZE
                        y = 0
                    if event.key == K_UP:
                        x = 0
                        y = -TILE_SIZE
                    if event.key == K_DOWN:
                        x = 0
                        y = TILE_SIZE
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game.inventory_button.button_clicked(480, 0, 20, 20):
                        button_clicked = not button_clicked
                    if self.game.save_button.button_clicked(590, 0, 20, 20):
                        with open('savegame', 'wb') as f:
                            pickle.dump(self.game, f, protocol=4)
                    if self.game.load_button.button_clicked(590, 50, 20, 20):
                        with open('savegame', 'rb') as f:
                            self.game = pickle.load(f)
                            self.game.view = View()
                #once button is pressed, check if x/y updated
                if event.type == KEYUP:
                    if x or y:
                        if self.game.move_player((x, y)) is False:
                            break
                        x = 0
                        y = 0
            if button_clicked:
                self.game.refresh(self.game.player.inventory)
            else:
                self.game.refresh(None)

loop = GameLoop()
loop.run()
