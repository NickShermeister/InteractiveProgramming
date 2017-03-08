import card_game
import deck_def
import hand_def
import game_constants

class Card(object):
    """The basic card behind everything.

    Attributes: Suit, Value, x (location), y (location), width, height, discarded, played, played_over"""

    def __init__(self, suit, value, startx = -1, starty = -1, width = game_constants.WIDTHCARD, height = game_constants.HEIGHTCARD, discarded = False, played = False):
        self.suit = suit        #number, suit
        self.value = value
        self.x = startx
        self.y = starty
        self.width = width
        self.height = height
        self.discarded = discarded
        self.played = played
        self.played_over = False        #Will become true if a card is played over it.
        self.opponent = False           #Gets set to True if it enters the opposing player's hand, which will cause it to not print what card it is.

    def contains_pt(self, pt):      #Returns True if a point is where the card is displayed; False otherwise.
        return (0 < (pt[0] - self.x) < self.width) and (0 < (pt[1] - self.y) < self.height)

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def play(self, newx, newy, hand, card_to_play_on = None):
        if card_to_play_on is None:
            if not self.discarded:
                if self.played:             #A way to tell if the card is in the field; if so, discard it.
                    self.discard(hand)
                else:                       #otherwise, move the card to the field (assuming it is a legal move).
                    self.x = newx
                    self.y = newy
                    self.played = True
                    hand.cards_in_hand.remove(self)
                    hand.player1_field.append(self)
        else:
            self.x = card_to_play_on.x
            self.y = card_to_play_on.y + game_constants.HEIGHTCARD
            hand.cards_in_hand.remove(self)
            hand.cards_on_field.append(self)
        for c in hand.cards_in_hand:    #relocate and then redisplay the screen with updated location of cards.
            c.x = (((game_constants.window_width * (5/8))/len(hand.cards_in_hand)) * hand.cards_in_hand.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2
        for c in hand.player1_field:
            c.x = (game_constants.window_width * (5/48) * hand.player1_field.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2
        for c in hand.cards_in_opponent:
            c.x = (((game_constants.window_width * (5/8))/len(hand.cards_in_opponent)) * hand.cards_in_hand.index(c)) + game_constants.window_width * (1.5/8) + game_constants.WIDTHCARD/2

    def discard(self, hand, discardx = game_constants.window_width * (1/8), discardy = game_constants.window_height * (1/2)):
        #for animated discard, will be more applicable later
        self.x = discardx
        self.y = discardy
        self.discarded = True
        hand.player1_field.remove(self)

    #def __str__(self):
    #    return("%d of %s" % self.value, self.suit)
