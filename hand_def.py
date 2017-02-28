import random
import pygame
import math

class Hand(object):
    """Defines both player hand and AI hand

    Attributes: cards"""

    def __init__(self, cards_in_hand = []):
        self.cards_in_hand = cards_in_hand

    def draw(self, number_of_cards):
        self.number_of_cards = number_of_cards
        for i in range(1, number_of_cards+1):
            self.add_card(deck.cards_in_deck[-i])

    def add_card(self, card):
        self.cards_in_hand.append(card)

    def __str__(self):
        return ', '.join(self.cards_in_hand)

    def remove_card(self, card):
        index = 0
        for x in range(len(self.cards_in_hand)-1):
            if str(self.cards_in_hand[x]) == str(card):
                #cards[i].delete_self()     #Will delete_self when we have a gme in front of us.
                self.cards_in_hand.remove(self.cards_in_hand[x])
                return
