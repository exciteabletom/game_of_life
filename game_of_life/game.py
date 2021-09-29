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

    def tick(self):
        cell_neighbours = {}
        for row in self.grid:
            for cell in row:
                live_neighbours = get_live_neighbour_count(cell, self.grid)
                cell_neighbours.update({cell: live_neighbours})

        for cell, neighbours in cell_neighbours.items():
            if cell.live and not 2 <= neighbours <= 3:
                self.grid[cell.row][cell.index].live = False
            elif not cell.live and neighbours == 3:
                self.grid[cell.row][cell.index].live = True
