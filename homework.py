from random import randint

import pygame

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600
BACK_COLOR = (87, 138, 52)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))


class Cub:
    def __init__(self, name: str):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.w = randint(50, 100)
        self.h = randint(50, 100)
        self.x = randint(0, int(SCREEN_WIDTH - self.w))
        self.y = 0
        self.speed = 1

    def move(self):
        if self.y < SCREEN_HIGHT:
            self.y += self.speed
        else:
            cubs.remove(self)


class Game:
    def __init__(self):
        return

    @staticmethod
    def draw():
        for cub in cubs:
            pygame.draw.rect(screen, cub.color, (cub.x, cub.y, cub.w, cub.h))

    @staticmethod
    def move():
        for cub in cubs:
            cub.move()


is_run = True
game = Game
cubs = []
while is_run:
    screen.fill(BACK_COLOR)
    game.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not len(cubs) >= 100:
            cubs.append(Cub("c"))
    game.move()
