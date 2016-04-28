"""
Constants used between files
May update these later to suit my needs
"""

#Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#size of each tile in the board, along with the number of rows and columns
TILE_SIZE = 48
ROW = 12
COLUMN = 10

#Items and weapons available to the game, along with other things
ITEMS = {
    "Seraph Robe": ("SERAPH", 7),
    "Vulnerary": ("HEALING", 10),
    "Concoction": ("HEALING", 20)
}
WEAPONS = {
    "Steel Axe": 12,
    "Iron Axe": 8,
    "Silver Axe": 16,
    "Hand Axe": 7
}

