import card_def
import card_game
import hand_def
import game_constants
import random
import pygame

class Deck(object):
    """The deck object defines a deck which both players can draw from.

    Attributes: deck_size, card_attributes, cards_in_deck, x, y, width, height"""

    def __init__(self, deck_size = 52, xloc = game_constants.window_width * (7/8), yloc = game_constants.window_height * (5/6), width = game_constants.WIDTHCARD, height = game_constants.HEIGHTCARD):
        '''deck_size is number of cards in deck (36)
        Initializes and creates the deck. Deck is a shuffled list of card objects with suit and value numbers.
        '''
        self.deck_size = deck_size
        self.card_attributes = {'suit':[0,1,2,3], 'number':[6,7,8,9,10,11,12,13,14]}        #This is coded for Durak; a normal deck would be 1-13.
        self.cards_in_deck = []
        for s in self.card_attributes['suit']:
            for n in self.card_attributes['number']:
                self.temp_card = card_def.Card(s, n, -1, game_constants.window_height * (2/3))
                self.cards_in_deck.append(self.temp_card)
        self.shuffle_deck(self.cards_in_deck)
        self.x = xloc
        self.y = yloc
        self.width = width
        self.height = height

    def draw(self, number_of_cards):
        '''Removes the top card of the deck
        '''
        self.number_of_cards = number_of_cards
        self.cards_in_deck = self.cards_in_deck[0:len(self.cards_in_deck)-self.number_of_cards]

    def contains_pt(self, pt):
        return (0 < pt[0] - self.x < self.width) and (0 < pt[1] - self.y < self.height)

    def shuffle_deck(self, cards_in_deck):
        '''Shuffles the deck
        '''
        return(random.shuffle(self.cards_in_deck))

    def play(self, hand):
        """Gives a card to a hand and removes said card from itself.
        """
        amt = 6 - len(hand.cards_in_hand)
        hand.draw(self)
        self.draw(amt)
        amt = 6 - len(hand.cards_in_opponent)
        hand.opponent_draw(self)
        self.draw(amt)
