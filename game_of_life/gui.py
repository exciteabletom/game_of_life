import enum
import sys
import time
from enum import Enum

import pygame

from .game import Game


class Colour(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class GUI:
    def __init__(self, window_size=(1280, 720)):
        self.WIDTH = window_size[0]
        self.HEIGHT = window_size[1]

        seed = [(2, 2), (3, 3), (4, 1), (4, 2), (4, 3)]
        self.game = Game(seed, int(self.HEIGHT / 20), int(self.WIDTH / 20))

        pygame.init()
        self.SCREEN = pygame.display.set_mode(window_size)
        self.CLOCK = pygame.time.Clock()

        self.SCREEN.fill(Colour.BLACK.value)

        count = 0
        while True:
            count += 1
            if count % 3 != 0:
                time.sleep(0.05)
                continue
            count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.SCREEN.fill(Colour.BLACK.value)

            self.game.tick()

            self.draw_grid()
            pygame.display.update()

    def update(self):
        pass

    def draw_grid(self):
        cell_size = 20
        for x in range(0, self.WIDTH, cell_size):
            row = int(x / 20)
            for y in range(0, self.HEIGHT, cell_size):
                cell = int(y / 20)
                rect = pygame.Rect(x, y, cell_size, cell_size)
                if self.game.grid[row][cell].live:
                    pygame.draw.rect(self.SCREEN, Colour.WHITE.value, rect)
                else:
                    pygame.draw.rect(self.SCREEN, Colour.WHITE.value, rect, 1)
