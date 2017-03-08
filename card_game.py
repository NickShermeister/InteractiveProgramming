import card_def
import card_game
import deck_def
import hand_def
import game_constants
import pygame
import sys
from pygame.locals import *

class DeckView(object):
    """A view that shows where the deck is, and how many cards are left in it.

        Attributes: visibility, model
    """
    def __init__(self,model):
        self.model = model
        self.visibility = True

    def draw(self, surface):        #Used to describe how the deck is drawn in pygame.
        model = self.model
        pygame.draw.rect(surface, game_constants.c_red, (int(model.x), int(model.y), model.width, model.height))

        font = pygame.font.SysFont("monospace", 15)
        deck_label = font.render(str(len(model.cards_in_deck)), 1, game_constants.c_black)
        screen.blit(deck_label, (model.x, model.y))
        if len(deck.cards_in_deck) > 0:         #As long as there are cards in the deck, it will be visible.
            trump_card_val_label = font.render(str(model.cards_in_deck[0].value), 1, game_constants.c_black)
            trump_card_suit_label = font.render(game_constants.suit_dict[model.cards_in_deck[0].suit], 1, game_constants.c_black)
            pygame.draw.rect(surface, game_constants.c_white, (int(model.x) - game_constants.WIDTHCARD * 1.2, int(model.y), model.width, model.height))
            screen.blit(trump_card_val_label, (model.x - game_constants.WIDTHCARD * 1.2, model.y))
            screen.blit(trump_card_suit_label, (model.x - game_constants.WIDTHCARD * 1.2, model.y + game_constants.HEIGHTCARD * 2/3))
        if len(deck.cards_in_deck) == 0:        #Auto-deletion of deck if there are no cards in it.
            self.visibility = False

    def delete(self):           #An alternative method to deleting the deck.
        self.visibility = False

class CardView(object):         #A view created for cards.
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.rect(surface, game_constants.c_white, (int(model.x), int(model.y), model.width, model.height))
        if not model.opponent:      #if the card isn't in the opponent's hand it will show its value and suit.
            font = pygame.font.SysFont("monospace", 15)
            val_label = font.render(str(model.value), 1, game_constants.c_black)
            suit_label = font.render(game_constants.suit_dict[model.suit], 1, game_constants.c_black)
            screen.blit(val_label, (model.x, model.y))
            screen.blit(suit_label, (model.x, model.y + game_constants.HEIGHTCARD * 2/3))

class MoveController(object):       #The basic controller for our game.
    def __init__(self, models):
        self.models = models

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for model in self.models:
                if model.contains_pt(pygame.mouse.get_pos()):
                    if model == deck:       #Important case checking if the deck size needs to be edited.
                        views.append(CardView(deck.cards_in_deck[len(deck.cards_in_deck)-1]))
                        controllers.append(MoveController([deck.cards_in_deck[len(deck.cards_in_deck)-1]]))
                        models.append(deck.cards_in_deck[len(deck.cards_in_deck)-1])
                    if not model.opponent:
                        model.play(model.x, model.y - game_constants.window_height * (1/6), hand)
                    else:
                        model.play(model.x, model.y + game_constants.window_height * (1/6), hand)
                    print("Here again.")
                    return True
        return False

class GameRules(object):
    """The rules that drive a normal game of Durak.

        Attributes: turn, trump, num_Cards_Played
    """
    def __init__(self, player_turn, deck_in):
        self.turn = player_turn      #player_turn is a boolean; True means player 1 is going False means player 2 is going.
        self.trump = deck_in.cards_in_deck[0].suit_label  #int of 0-3 definining the trump suit
        self.num_Cards_Played = 0
        self.beat = False

    def playable_defense(self, field_card, hand_card):      #Checks for the playability of a card on another card defensively.
        if not field.Card.played_over:
            self.num_cards_played += 1
            if field_card.suit == self.trump and hand_card.suit != self.trump:
                return False
            elif field_card.suit ==self.trump and hand_card.suit == self.trump:
                if field_card.value > hand_card.value:
                    return False
                else:
                    return True
            elif hand_card.suit == self.trump:
                return True
            elif hand_card.suit == field_card.suit:
                if field_card.value > hand_card.value:
                    return False
                else:
                    return True
            else:
                return False
        else:
            return False

    def playable_offense(self, hand_in, card_in):           #Checks to see if a card can be played offensively.
        if num_cards_played < 1:
            num_cards_played += 1
            return True
        elif num_cards_played >= game_constants.max_cards_played:
            return False
        else:
            if card_in.value in hand_in.cards_in_field:
                return True
            else:
                return False

    def play_card(self, field_card, play_card, hand):
        play_card.play(field_card.x, field_card.x + int(game_constants.HEIGHTCARD), hand)

    def beat_turn(self):                    #Resets based on a successful defense.
        self.turn = not self.turn
        self.num_cards_played = 0
        self.beat = True

    def lost_turn(self):                    #Resets based on a successful offense.
        self.num_cards_played = 0
        self.beat = False

    def cleanup(self, hands, deck):
        if self.beat == False:
            if self.turn:
                for card in hands.cards_in_field: #TODO: CHANGE SO IT ADDS BOTH LEVELS OF CARDS
                    hands.cards_in_opponent.append(card)
            else:
                for card in hands.cards_in_field: #TODO: CHANGE SO IT ADDS BOTH LEVELS OF CARDS
                    hands.cards_in_hand.append(card)
            for card in hands.cards_in_field:   #TODO: CHANGE THIS SO IT DISCARDS BOTH LEVELS OF CARDS
                card.discard()


if __name__ == "__main__":
    pygame.init()

    deck = deck_def.Deck(36)
    hand = hand_def.Hand(game_constants.starting_hand_size, deck)
    opponent_hand = hand_def.Hand(game_constants.starting_hand_size, deck)
    testcard = card_def.Card(0, 0, 100, 100)            #just mark a card as "opponent" to block it printing anything.
    testcard.opponent = True


    pygame.display.set_caption('DURAK')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((game_constants.window_width, game_constants.window_height))

    views = [DeckView(deck)]
    controllers = [MoveController([deck])]
    models = [deck]

    testview = CardView(testcard)

    for c in hand.cards_in_hand:
        views.append(CardView(c))
        controllers.append(MoveController([c]))
        models.append(c)

    # for c in ophand.cards_in_hand:
    #     c.opponent = True
    #     views.append(CardView(c))
    #     controllers.append(MoveController([c]))
    #     models.append(c)

    running = True
    deckalive = True
    while running:
        pygame.display.update()
        clock.tick(game_constants.fps)
        screen.fill(game_constants.c_black)
        for event in pygame.event.get():
            for cont in controllers:
                if cont.handle_event(event):
                    break
            if event.type == pygame.QUIT:
                running = False
        for view in views:
            view.draw(screen)
        testview.draw(screen)
        if deckalive:
            if not views[0].visibility:
                views = views[1:]
                controllers = controllers[1:]
                models = models[1:]
                deckalive = False

    pygame.quit()
