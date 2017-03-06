import card_def
import card_game
import deck_def
import hand_def
import game_constants
import pygame
import sys
from pygame.locals import *

class DeckView(object):
    def __init__(self,model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.rect(surface, game_constants.c_red, (int(model.x), int(model.y), model.width, model.height))

        font = pygame.font.SysFont("monospace", 15)
        label = font.render(str(len(model.cards_in_deck)), 1, game_constants.c_black)
        screen.blit(label, (model.x, model.y))

class CardView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.rect(surface, game_constants.c_white, (int(model.x), int(model.y), model.width, model.height))

        font = pygame.font.SysFont("monospace", 15)
        val_label = font.render(str(model.value), 1, game_constants.c_black)
        screen.blit(val_label, (model.x, model.y))
        suit_label = font.render(game_constants.suit_dict[model.suit], 1, game_constants.c_black)
        screen.blit(suit_label, (model.x, model.y + game_constants.HEIGHTCARD * 2/3))

class MoveController(object):
    def __init__(self, models):
        self.models = models

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for model in self.models:
                if model.contains_pt(pygame.mouse.get_pos()):
                    if model == deck:
                        views.append(CardView(deck.cards_in_deck[len(deck.cards_in_deck)-1]))
                        controllers.append(MoveController([deck.cards_in_deck[len(deck.cards_in_deck)-1]]))
                        models.append(deck.cards_in_deck[len(deck.cards_in_deck)-1])
                    model.play(model.x, model.y - 100, hand)
                    break
        if event.type == pygame.KEYDOWN:
            for model in self.models:
                model.reset()

if __name__ == "__main__":
    pygame.init()

    deck = deck_def.Deck(36)
    hand = hand_def.Hand(5, deck)

    pygame.display.set_caption('DURAK')
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((game_constants.window_width, game_constants.window_height))

    views = [DeckView(deck)]
    controllers = [MoveController([deck])]
    models = [deck]

    for c in hand.cards_in_hand:
        views.append(CardView(c))
        controllers.append(MoveController([c]))
        models.append(c)

    running = True

    while running:
        pygame.display.update()
        clock.tick(game_constants.fps)
        screen.fill(game_constants.c_black)
        for event in pygame.event.get():
            for cont in controllers:
                cont.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
        for view in views:
            view.draw(screen)

    pygame.quit()
