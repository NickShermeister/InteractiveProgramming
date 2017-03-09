import card_def
import card_game
import deck_def
import game_constants

class Hand(object):
    """Defines both player hand and AI hand

    Has morphed into a field definition of some sort over time.

    Attributes: cards_in_hand, cards_in_field, turn"""

    def __init__(self, hand_size, deck, cards_in_hand = [], cards_in_field = [], cards_top_field = [], cards_in_opponent = []):
        self.cards_in_hand = cards_in_hand
        self.player1_field = cards_in_field         #The cards being played offensively in the field.
        self.player2_field = cards_top_field        #The cards being played defensively on the field.
        self.cards_in_opponent = cards_in_opponent
        self.draw(hand_size, deck)
        deck.draw(hand_size)
        self.opponent_draw(hand_size, deck)
        deck.draw(hand_size)

    def draw(self, number_of_cards, deck):
        self.number_of_cards = number_of_cards
        for i in range(1, number_of_cards+1):
            self.add_card(deck.cards_in_deck[-i])
        for c in self.cards_in_hand:
            c.x = (((game_constants.window_width * (5/8))/len(self.cards_in_hand)) * self.cards_in_hand.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2

    def opponent_draw(self, number_of_cards, deck):
        self.number_of_cards = number_of_cards
        for i in range(1, number_of_cards+1):
            self.opponent_add_card(deck.cards_in_deck[-i])
        for c in self.cards_in_opponent:
            c.y = 75
            c.x = (((game_constants.window_width * (5/8))/len(self.cards_in_opponent)) * self.cards_in_opponent.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2


    def add_card(self, card):
        self.cards_in_hand.append(card)

    def opponent_add_card(self, card):
        self.cards_in_opponent.append(card)

    def __str__(self):
        return ', '.join(self.cards_in_hand)
