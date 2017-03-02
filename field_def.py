import card_def
import card_game
import deck_def
import hand_def
import pygame

import sys
from pygame.locals import *

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class CardView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.rect(surface, BLUE, (int(model.x), int(model.y), model.width, model.height))

class DeckView(object):
    def __init__(self,model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.rect(surface, RED, (int(model.x), int(model.y), model.width, model.height))

class MoveController(object):
    def __init__(self, models):
        self.models = models

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for model in self.models:
                if model.contains_pt(pygame.mouse.get_pos()):
                    model.play(model.x, model.y - 100)
                    break
        if event.type == pygame.KEYDOWN:
            for model in self.models:
                model.reset()

class DrawController(object):
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


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    card1 = card_def.Card(0, 0, 200, 320)
    card2 = card_def.Card(0, 0, 300, 320)
    deck = deck_def.Deck()
    models = [card1, card2, deck]

    views = []
    views.append(CardView(card1))
    views.append(CardView(card2))
    views.append(DeckView(deck))
    # views.append(BallEnergyView(card))

    controllers = []

    controllers.append(MoveController([card1]))
    controllers.append(MoveController([card2]))

    running = True
    while running:
        for event in pygame.event.get():
            for cont in controllers:
                cont.handle_event(event)
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        for view in views:
            view.draw(screen)

        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
