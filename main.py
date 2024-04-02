from tkinter import *
from settings import *
import random
import Cell_Logic


def main():
    global root, canvas, this_turn

    # creates window
    root = Tk()
    root.title('The game of life')
    root.geometry(f'{width}x{height}')
    root.resizable(False, False)

    # creates canvas
    canvas = Canvas(root, width=width, height=height, background='pink')
    canvas.place(x=0, y=0)

    this_turn = {}
    generate_cells()
    turn(this_turn)

    root.mainloop()


def generate_cells():
    for x in range(width // cell_size):
        for y in range(height // cell_size):
            alive = 1 if random.randint(0, 100) < 50 else 0
            cell = [(x, y), alive]
            this_turn[(x, y)] = cell


def turn(dict_of_cells):

    render()
    next_turn = {}

    # rules
    for cell in dict_of_cells.values():
        (x, y), alive = cell
        live_neighbors = Cell_Logic.live_neighbors(cell, dict_of_cells)
        if live_neighbors < 2:
            cell = [(x, y), 0]
        elif (live_neighbors == 2 or live_neighbors == 3) and alive == 1:
            cell = [(x, y), 1]
        elif live_neighbors > 3:
            cell = [(x, y), 0]
        elif not alive == 1 and live_neighbors == 3:
            cell = [(x, y), 1]

        next_turn[(x, y)] = cell

    dict_of_cells.update(next_turn)
    root.after(1, turn, dict_of_cells)


def render():

    # resets canvas
    canvas.delete(ALL)

    # draws cells
    for (x, y), alive in this_turn.values():
        color = 'white' if alive == 1 else 'black'

        canvas.create_rectangle(
            x * cell_size,
            y * cell_size,
            x * cell_size + cell_size,
            y * cell_size + cell_size,
            fill=color
        )

    # draws the grid
    [canvas.create_line(0, i*cell_size, width, i*cell_size, fill='dark green') for i in range(width//cell_size)]
    [canvas.create_line(i*cell_size, 0, i*cell_size, height, fill='dark green') for i in range(height//(cell_size//2))]


if __name__ == "__main__":
    main()
