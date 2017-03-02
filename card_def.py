import random
import pygame
import math

WIDTHCARD = 40
HEIGHTCARD = 60

class Card(object):
    """The basic card behind everything.

    Attributes: Suit, Value"""

    def __init__(self, suit, value, startx = -1, starty = -1, width = WIDTHCARD, height = HEIGHTCARD, discarded = False, played = False):
        self.suit = suit        #number, suit
        self.value = value
        self.x = startx
        self.y = starty
        self.width = width
        self.height = height
        self.discarded = discarded
        self.played = played

    def contains_pt(self, pt):
        return (0 < pt[0] - self.x < self.width) and (0 < pt[1] - self.y < self.height)

    def play(self, newx, newy):
        if not self.discarded:
            if (self.played):
                self.discard() #TODO: IMPLEMENT; MAKE THE CARD MOVE TO THE APPROPRIATE SPOT ON THE BOARD.
            else:
                self.x = newx
                self.y = newy
                self.played = True

    def discard(self, discardx = 100, discardy = 400): #for animated discard, will be more applicable later
        self.x = discardx
        self.y = discardy
        self.discarded = True

    #def __str__(self):
    #    return("%d of %s" % self.value, self.suit)
