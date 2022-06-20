"""
class file for the game board

"""
import enum
import figures


# creating a classification system for cell types
class CellType(enum.Enum):
    origin = 1
    live = 2
    dead = 3


# base class for a game board, has attributes 'size'
class GameBoard:
    def __init__(self, size):
        self.grid = Grid(size)  # the size of the game board represented as a grid [size x size]
        self.solved = False  # whether the game has been won or not

    # sets the game status to 'won' (solved)
    def game_won(self):
        self.solved = True

    # takes the list of figures, and places them on the gameboard
    def populate_board(self, figures_list):
        for figure in figures_list:
            self.grid.place_figure(figure)


class Grid:
    def __init__(self, length):
        self.axis_length = length  # the x and y-axis will both share the same length
        self.grid = self.construct_grid()  # the grid object will construct itself as soon as it is initialized

    # will construct a grid with ordered x, and y coordinate pairs (NOT CELLS!)
    def construct_grid(self):
        constructed_grid = []

        # will count from 0 up to the length of the x-axis
        for y in range(0, self.axis_length):
            # will count from 0 up to the length of the y-axis
            for x in range(0, self.axis_length):
                new_cell = Cell(x, y)
                constructed_grid.append(new_cell)

        return constructed_grid

    # takes a given figure, and places it on the grid
    def place_figure(self, figure):
        pass

    # goes through the grid and numbers each figure origin cell as per Figure Logic puzzle logic, which is this:
    # each origin cell is enumerated from 1, up to n, where n is the integer count of UNIQUE origin cells on the grid
    # to clarify: if an across, and down figure have the same origin cell-- they will share the same number identifier
    def number_origins(self):
        pass

    # outputs the coordinates of all cells on the grid (formatted) (FOR TESTING IF THE GRID IS CONSTRUCTED PROPERLY)
    def output_grid(self):
        grid_output = ""
        for cell in range(0, len(self.grid)):
            # grid_output += str(self.grid[cell].retrieve_cell_coords())
            grid_output += "[ ]"  # for outputting a blank board!

            # add a new line to separate rows in a formatted form
            if ((cell - (self.axis_length - 1)) % self.axis_length) == 0:
                grid_output += "\n"

        print(grid_output)


class Cell:
    def __init__(self, x_coord, y_coord):
        self.coordinates = [x_coord, y_coord]
        self.contents = ""
        self.associated_figures = []
        self.cell_type = CellType.dead  # by default, any created cells are dead until specified otherwise

    def retrieve_cell_coords(self):
        return self.coordinates

    # changes the specified cell into an origin cell
    def make_origin(self):
        self.cell_type = CellType.origin

    # changes the specified cell into a live cell
    def make_cell_live(self):
        self.cell_type = CellType.live


# TESTING BLOCK:
test_board = GameBoard(20)
test_board.grid.output_grid()
