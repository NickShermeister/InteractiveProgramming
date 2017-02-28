import random
import pygame
import math

class Card(object):
    """The basic card behind everything.

    Attributes: Suit, Value"""

    def __init__(self, suit, value):
        self.suit = suit        #number, suit
        self.value = value

    #def __str__(self):
    #    return("%d of %s" % self.value, self.suit)
