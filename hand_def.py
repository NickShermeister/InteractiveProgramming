import random
import pygame
import math

class Hand(object):
    """Defines both player hand and AI hand

    Attributes: cards"""

    def __init__(self, cards = []):
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def __str__(self):
        return ', '.join(self.cards)

    def remove_card(self, card):
        index = 0
        for x in range(len(self.cards)-1):
            if str(self.cards[x]) == str(card):
                #cards[i].delete_self()     #Will delete_self when we have a gme in front of us.
                self.cards.remove(self.cards[x])
                return
