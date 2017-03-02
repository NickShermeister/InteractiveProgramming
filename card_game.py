import math
import random
import pygame

class Card(object):
    """The basic card behind everything.

    Attributes: Suit, Value"""

    def __init__(self, suit, value):
        self.suit = suit        #number, suit
        self.value = value

    #def __str__(self):
    #    return("%d of %s" % self.value, self.suit)

class Deck(object):

    def __init__(self, deck_size):
        '''deck_size is number of cards in deck (36)
        Initializes and creates the deck. Deck is a shuffled list of card objects with suit and value numbers.
        '''
        self.deck_size = deck_size
        self.card_attributes = {'suit':[0,1,2,3], 'number':[6,7,8,9,10,11,12,13,14]}
        self.cards_in_deck = []
        for s in self.card_attributes['suit']:
            for n in self.card_attributes['number']:
                self.temp_card = Card(s, n)
                self.cards_in_deck.append(self.temp_card)
        self.shuffle_deck(self.cards_in_deck)

    def draw(self, number_of_cards):
        '''Removes the top card of the deck
        '''
        self.number_of_cards = number_of_cards
        self.cards_in_deck = self.cards_in_deck[0:len(self.cards_in_deck)-self.number_of_cards]

    def shuffle_deck(self, cards_in_deck):
        '''Shuffles the deck
        '''
        return(random.shuffle(self.cards_in_deck))

class Hand(object):
    """Defines both player hand and AI hand

    Attributes: cards"""

    def __init__(self, hand_size, deck, cards_in_hand = []):
        self.deck = deck
        self.hand_size = hand_size
        self.cards_in_hand = cards_in_hand
        self.draw(hand_size)

    def draw(self, number_of_cards):
        self.number_of_cards = number_of_cards
        for i in range(1, number_of_cards+1):
            self.add_card(deck.cards_in_deck[-1])
            deck.draw(1)

    def add_card(self, card):
        self.cards_in_hand.append(card)

    def __str__(self):
        return ', '.join(self.cards_in_hand)

    def remove_card(self, card):
        index = 0
        for x in range(len(self.cards_in_hand)-1):
            if str(self.cards_in_hand[x]) == str(card):
                #cards[i].delete_self()     #Will delete_self when we have a game in front of us.
                self.cards_in_hand.remove(self.cards_in_hand[x])
                return


if __name__ == "__main__":
    pygame.init()

    deck = Deck(36)
    hand = Hand(5, deck)

    window_width = 800
    window_height = 600
    c_white = (255,255,255)

    pygame.display.set_caption('DURAK')
    clock = pygame.time.Clock()
    gameDisplay = pygame.display.set_mode((window_width, window_height))

    running = True

    while running:
        pygame.display.update()
        clock.tick(60)
        gameDisplay.fill(c_white)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
