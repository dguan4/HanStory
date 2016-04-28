"""
Combat class for the combat system
"""

import random
import time


class Combat:

    def __init__(self, player, monster, view):
        """
        Simply initialize with both the player and the monster doing the combat
        :param player: player to do combat with
        :param monster: monster to do combat with
        :param view: view of the combat system
        :return:
        """
        self.player = player
        self.monster = monster
        self.view = view

    def init_combat(self):
        """
        Initiates combat. For now, since I have no way to define turns, player always goes first
        This continues until either side's hp is 0
        :return:
        """
        while self.player.hp > 0 and self.monster.hp > 0:
            #player goes first
            self.player_hit()
            if self.player.hp > 0 and self.monster.hp > 0:
                self.monster_hit()
            if self.player.hp > 0 and self.monster.hp > 0:
                if self.player.stats['spd'] >= self.monster.stats['spd']+4:
                    self.player_hit()
                if self.monster.stats['spd'] >= self.player.stats['spd']+4:
                    self.monster_hit()
        return self.player.hp, self.monster.hp

    def monster_hit(self):
        """
        Calculates the monster hit chance and attacks if possible
        :return:
        """
        monster_hit_chance = random.random()
        monster_chance = random.random()
        if monster_chance >= monster_hit_chance:
            damage = self.monster.attack(self.player.stats['def'])
            self.player.receive_damage(damage)
            self.combat_hit_miss(False, True)
        else:
            self.combat_hit_miss(False, False)
        time.sleep(1)

    def player_hit(self):
        """
        Calculates the player hit chance and attacks if possible
        :return:
        """
        player_hit_chance = random.random()
        player_chance = random.random()
        if player_chance >= player_hit_chance:
            damage = self.player.attack(self.monster.stats['def'])
            self.monster.receive_damage(damage)
            self.combat_hit_miss(True, True)
        else:
            self.combat_hit_miss(True, False)
        time.sleep(1)

    def combat_hit_miss(self, turn, hit):
        """
        Draws the combat and displays hit or miss
        :param turn: whose turn it is (T/F)
        :param hit: whether the attack hit or not
        :return:
        """
        self.view.draw_combat(self.player, self.monster, turn, hit)
