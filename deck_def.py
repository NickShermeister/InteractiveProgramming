import random

class Deck(object):

    def __init__(self, deck_size):
        #deck_size is 36
        self.deck_size = deck_size
        card_attributes = {'suit':[0,1,2,3], 'number':[6,7,8,9,10,11,12,13,14]}
        cards_in_deck = []
        for s in card_attributes['suit']:
            for n in card_attributes['number']:
                temp_card = Card(s, n)
                cards_in_deck.append(temp_card)
        print(cards_in_deck)

    def draw(self):


    def shuffle_deck(self, cards_in_deck):
        random.shuffle(cards_in_deck)
