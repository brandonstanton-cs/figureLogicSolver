"""
class file for the game board

"""

from figures import Figure

# base class for a game board, has attributes 'size'
class GameBoard:
    def __init__(self, size):
        self.grid = [size, size]  # the size of the game board represented as a grid [size x size]
        self.dead_cells = []  # list of cells that are blacked out, and cannot contain a figure, or number
        self.solved = False  # whether the game has been won or not

    # add a location on the grid to the list of dead cells (blacked out game cells)
    def add_dead_cell(self, location):
        self.dead_cells.append(location)

    # sets the game status to 'won' (solved)
    def game_won(self):
        self.solved = True

    # populates the entire game board, using the list of figures given
    def populate_board(self, figures_list):
        for figure in figures_list:
            self.designate_squares(figure)

    # takes a given figure, and designates which squares it occupies on the game board
    def designate_squares(self, figure):
        # the calculation for determining which square is directly below the origin:
        if figure.feature is 'down':
            for i in range(figure.origin[])
        elif:



