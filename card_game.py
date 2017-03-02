import card_def
import card_game
import deck_def
import hand_def
import game_constants
import pygame
import sys
from pygame.locals import *

class CardView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.rect(surface, c_white, (int(model.x), int(model.y), model.width, model.height))

class MoveController(object):
    def __init__(self, models):
        self.models = models

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for model in self.models:
                if model.contains_pt(pygame.mouse.get_pos()):
                    model.play(300, 300)
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

    views = []
    controllers = []
    models = []

    for c in hand.cards_in_hand:
        views.append(CardView(c))
        controllers.append(MoveController([c]))
        models.append(c)

    running = True

    while running:
        pygame.display.update()
        clock.tick(60)
        screen.fill(game_constants.c_black)
        for event in pygame.event.get():
            for cont in controllers:
                cont.handle_event(event)
            if event.type == pygame.QUIT:
                running = False
        for view in views:
            view.draw(screen)

    pygame.quit()
