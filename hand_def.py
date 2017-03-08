import card_def
import card_game
import deck_def
import game_constants

class Hand(object):
    """Defines both player hand and AI hand

    Attributes: cards_in_hand, cards_in_field"""

    def __init__(self, hand_size, deck, cards_in_hand = [], cards_in_field = []):
        self.cards_in_hand = cards_in_hand
        self.cards_in_field = cards_in_field
        self.draw(hand_size, deck)
        deck.draw(hand_size)

    def draw(self, number_of_cards, deck):
        self.number_of_cards = number_of_cards
        for i in range(1, number_of_cards+1):
            self.add_card(deck.cards_in_deck[-i])
        for c in self.cards_in_hand:
            c.x = (((game_constants.window_width * (5/8))/len(self.cards_in_hand)) * self.cards_in_hand.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2

    def add_card(self, card):
        self.cards_in_hand.append(card)

    def update(self):
        for c in self.cards_in_hand:
            c.x = (((game_constants.window_width * (5/8))/len(self.cards_in_hand)) * self.cards_in_hand.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2
        for c in self.cards_in_field:
            c.x = (game_constants.window_width * (5/48) * self.cards_in_field.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2

    def __str__(self):
        return ', '.join(self.cards_in_hand)
