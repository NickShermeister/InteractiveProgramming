import random

class Deck(object):

    def __init__(self, deck_size):
        '''deck_size is number of cards in deck (36)
        Initializes and creates the deck. Deck is a shuffled list of card objects with suit and value numbers.
        '''
        self.deck_size = deck_size
        self.card_attributes = {'suit':[0,1,2,3], 'number':[6,7,8,9,10,11,12,13,14]}
        self.cards_in_deck = []
        for s in card_attributes['suit']:
            for n in card_attributes['number']:
                self.temp_card = Card(s, n)
                self.cards_in_deck.append(self.temp_card)
        self.shuffle_deck(cards_in_decks)

    def draw(self):
        '''Removes the top card of the deck
        '''
        self.cards_in_deck = self.cards_in_deck[0, len(self.cards_in_deck)-1]

    def shuffle_deck(self, cards_in_deck):
        '''Shuffles the deck
        '''
        return(random.shuffle(self.cards_in_deck))
