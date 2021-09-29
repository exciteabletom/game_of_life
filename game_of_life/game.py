import copy
from pprint import pprint

from .cell import Cell


def get_live_neighbour_count(cell: Cell, grid) -> int:
    count = 0
    for row_offset in (-1, 0, 1):
        try:
            row = grid[cell.row + row_offset]
            for index_offset in (-1, 0, 1):
                if row[cell.index + index_offset].live:
                    count += 1
        except IndexError:
            pass

    if cell.live:
        count -= 1

    return count


class Game:
    def __init__(self, seed, width, height):
        self.grid: list[list[Cell]] = []
        for h in range(height):
            self.grid.append([])
            for w in range(width):
                self.grid[-1].append(Cell(h, w))

        for row, index in seed:
            self.grid[row][index].live = True

    def print_grid(self, grid=None):
        if grid is None:
            grid = self.grid

        for row in grid:
            for cell in row:
                if cell.live:
                    print("x", end="")
                else:
                    print("o", end="")

            print("")

    def tick(self):
        grid_copy = copy.deepcopy(self.grid)
        for row_num, row in enumerate(grid_copy):
            for index, cell in enumerate(row):
                live_neighbours = get_live_neighbour_count(cell, grid_copy)
                if cell.live and not 2 <= live_neighbours <= 3:
                    self.grid[row_num][index].live = False
                elif not cell.live and live_neighbours == 3:
                    self.grid[row_num][index].live = True