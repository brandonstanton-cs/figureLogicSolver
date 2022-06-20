"""
class file for the game board

"""


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

    # fills in the game board with all the locations of the figures
    def populate_board(self, figures_list):
        self.solved = True

