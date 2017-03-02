import card_game
import deck_def
import hand_def
import game_constants

class Card(object):
    """The basic card behind everything.

    Attributes: Suit, Value"""

    def __init__(self, suit, value, startx = -1, starty = -1, width = game_constants.WIDTHCARD, height = game_constants.HEIGHTCARD, discarded = False, played = False):
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

    def play(self, newx, newy, hand):
        if not self.discarded:
            if (self.played):
                self.discard(hand) #TODO: IMPLEMENT; MAKE THE CARD MOVE TO THE APPROPRIATE SPOT ON THE BOARD.
            else:
                self.x = newx
                self.y = newy
                self.played = True
        for c in hand.cards_in_hand:
            c.x = (((game_constants.window_width * (5/8))/len(hand.cards_in_hand)) * hand.cards_in_hand.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2


    def discard(self, hand, discardx = game_constants.window_width * (1/8), discardy = game_constants.window_height * (1/2)):
        #for animated discard, will be more applicable later
        self.x = discardx
        self.y = discardy
        self.discarded = True
        hand.cards_in_hand.remove(self)

    #def __str__(self):
    #    return("%d of %s" % self.value, self.suit)
