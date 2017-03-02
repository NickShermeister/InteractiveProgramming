
import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WIDTHCARD = 40
HEIGHTCARD = 60


class Card(object):
    def __init__(self, startx, starty, width = WIDTHCARD, height = HEIGHTCARD):
        self.width = width
        self.height = height
        self.startx = startx
        self.starty = starty
        self.reset()

    def reset(self):
        self.x = self.startx
        self.y = self.starty
        self.dy = 0

    def contains_pt(self, pt):
        return (0 < pt[0] - self.x < self.width) and (0 < pt[1] - self.y < self.height)

    def play(self):
        self.y = 100


class CardView(object):
    def __init__(self, model):
        self.model = model

    def draw(self, surface):
        model = self.model
        pygame.draw.rect(surface, BLUE, (int(model.x), int(model.y), model.width, model.height))


class MoveController(object):
    def __init__(self, models):
        self.models = models

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for model in self.models:
                if model.contains_pt(pygame.mouse.get_pos()):
                    model.play()
                    break
        if event.type == pygame.KEYDOWN:
            for model in self.models:
                model.reset()


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    card1 = Card(200, 320)
    card2 = Card(300, 320)
    models = [card1, card2]

    views = []
    views.append(CardView(card1))
    views.append(CardView(card2))
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
