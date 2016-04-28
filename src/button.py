"""
Button class for doing actions
"""

import pygame


class Button:

    def __init__(self, text, x, y, width, height, action=None):
        """
        Creates a button at a location and some text
        :param text: text to display
        :param x: x location
        :param y: y location
        :param width: width of button
        :param height: height of button
        :param action: action to perform
        :return:
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action

    def button_clicked(self, x, y, width, height):
        """
        Checks if the button is clicked
        :param x:
        :param y:
        :param width:
        :param height:
        :param action:
        :return:
        """
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+width > mouse[0] > x and y+height > mouse[1] > y:
            if click[0] == 1:
                return True
        return False
