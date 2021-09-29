#!/usr/bin/env python3
import time
from game_of_life import game
from game_of_life.gui import GUI

glider_seed = [(2, 2), (3, 3), (4, 1), (4, 2), (4, 3)]
g = game.Game(glider_seed, 50, 50)

while True:
    GUI()
