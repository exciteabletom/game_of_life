import sys
from enum import Enum

import pygame

from .game import Game


class Colour(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


class GUI:
    def __init__(self, window_size=(1280, 720), cell_size=10):
        self.CELL_SIZE = cell_size
        self.WIDTH = window_size[0]
        self.HEIGHT = window_size[1]

        pygame.init()
        self.SCREEN = pygame.display.set_mode(window_size)
        self.CLOCK = pygame.time.Clock()

        self.SCREEN.fill(Colour.BLACK.value)

        self.game = Game([], self.WIDTH, self.HEIGHT)
        self.active = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        status = True
                    else:
                        status = False

                    pos = pygame.mouse.get_pos()
                    clicked_rects = [rect for rect in self.rects if rect.collidepoint(pos)]
                    for rect in clicked_rects:
                        row = int(rect.x / self.CELL_SIZE)
                        cell = int(rect.y / self.CELL_SIZE)
                        self.game.grid[row][cell].live = status

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.active = not self.active

            self.SCREEN.fill(Colour.BLACK.value)

            if self.active:
                self.game.tick()

            self.draw_grid()
            pygame.display.update()

    def draw_grid(self):
        self.rects = []
        for x in range(0, self.WIDTH, self.CELL_SIZE):
            row = int(x / self.CELL_SIZE)
            for y in range(0, self.HEIGHT, self.CELL_SIZE):
                cell = int(y / self.CELL_SIZE)
                rect = pygame.Rect(x, y, self.CELL_SIZE, self.CELL_SIZE)
                self.rects.append(rect)
                if self.game.grid[row][cell].live:
                    pygame.draw.rect(self.SCREEN, Colour.WHITE.value, rect)
                else:
                    pygame.draw.rect(self.SCREEN, Colour.WHITE.value, rect, 2)
