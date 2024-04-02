from settings import *

def get_cell_by_coords(coords, dictionare:dict):
    return dictionare[coords]


def get_neighbors(cell, dictionare:dict):
    (cell_x, cell_y), alive = cell
    neighbors = []
    for x in range(cell_x - 1, cell_x + 2):
        for y in range(cell_y - 1, cell_y + 2):
            if (x < 0 or y < 0) or (x == cell_x and y == cell_y) or (
                    x >= (width / cell_size) or y >= (height / cell_size)):
                continue
            else:
                coords = (x, y)
                cell = get_cell_by_coords(coords, dictionare)
                neighbors.append(cell)
    return neighbors


def live_neighbors(cell, dict):
    count = 0
    for coords, alive in get_neighbors(cell, dict):
        if alive == 1:
            count += 1

    return count