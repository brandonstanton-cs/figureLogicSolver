"""
class file for the game board

"""
import enum
from figures import Figure


# creating a classification system for cell types
class CellType(enum.Enum):
    origin = 1
    live = 2
    dead = 3


# base class for a game board, has attributes 'size'
class GameBoard:
    def __init__(self, x_size, y_size):
        self.board = Grid(x_size, y_size)  # the size of the game board represented as a grid [size x size]
        self.figure_list = []  # collection of all the figure data for the game
        self.solved = False  # whether the game has been won or not

    # sets the game status to 'won' (solved)
    def game_won(self):
        self.solved = True

    # takes the list of figures, and places them on the gameboard
    def populate_board(self):
        cell_coords_list = self.board.list_cell_coords()
        for figure in self.figure_list:

            if figure.origin in cell_coords_list:
                print("found cell!, making origin point...")
                figure_origin_cell = self.board.pinpoint_cell(figure.origin[0], figure.origin[1])
                figure_origin_cell.make_origin()

    # queries the user and generates a list of figures
    def collect_figures(self):
        # collect across figures first
        print("Collecting Across Figures...")
        while True:
            figure_length = int(input("How many digits does the figure contain?"))
            figure_origin_x = int(input("What is the figure's x axis? (left is 0)"))
            figure_origin_y = int(input("What is the figure's y axis? (top is 0)"))
            new_figure = Figure(figure_length, figure_origin_x, figure_origin_y)
            self.figure_list.append(new_figure)
            if input("Down Figure Time?") == 'next':
                break

        print("Collecting Down Figures...")
        while True:
            figure_length = int(input("How many digits does the figure contain?"))
            figure_origin_x = int(input("What is the figure's x axis? (left is 0)"))
            figure_origin_y = int(input("What is the figure's y axis? (top is 0)"))
            new_figure = Figure(figure_length, figure_origin_x, figure_origin_y, False)
            self.figure_list.append(new_figure)
            if input("Done?") == 'next':
                break

        print("Complete! printing out figures...")

        for figure in self.figure_list:
            figure.describe_figure()


class Grid:
    def __init__(self, x_length, y_length):
        self.x_axis_length = x_length
        self.y_axis_length = y_length
        self.grid = []  # the grid will need to be constructed by method call

    # will construct a grid with ordered x, and y coordinate pairs (NOT CELLS!)
    def construct_grid(self):
        constructed_grid = []

        # will count from 0 up to the length of the x-axis
        for y in range(0, self.y_axis_length):
            # will count from 0 up to the length of the y-axis
            for x in range(0, self.x_axis_length):
                new_cell = Cell(x, y)
                constructed_grid.append(new_cell)

        self.grid = constructed_grid

    # goes through the grid and numbers each figure origin cell as per Figure Logic puzzle logic, which is this:
    # each origin cell is enumerated from 1, up to n, where n is the integer count of UNIQUE origin cells on the grid
    # to clarify: if an across, and down figure have the same origin cell-- they will share the same number identifier
    def number_origins(self):
        pass

    def list_cell_coords(self):
        cell_coords_list = []
        for cell in range(0, len(self.grid)):
            cell_coords_list.append(self.grid[cell].retrieve_cell_coords())
        return cell_coords_list

    # TODO take above method, and replace with below methods (for cleaner access!)

    # using x and y coordinates, specify a specific cell
    def pinpoint_cell(self, x_coord, y_coord):
        for cell in self.grid:
            if cell.coordinates == [x_coord, y_coord]:
                return cell

    # outputs the coordinates of all cells on the grid (formatted) (FOR TESTING IF THE GRID IS CONSTRUCTED PROPERLY)
    def output_grid(self):
        grid_output = ""
        for cell in range(0, len(self.grid)):
            if self.grid[cell].cell_type == CellType.origin:
                grid_output += "[ ]"
            elif self.grid[cell].cell_type == CellType.live:
                grid_output += "[ ]"
            else:
                grid_output += "[x]"

            # add a new line to separate rows in a formatted form
            if ((cell - (self.x_axis_length - 1)) % self.x_axis_length) == 0:
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
current_game = GameBoard(6, 7)
current_game.board.construct_grid()
current_game.board.output_grid()
current_game.collect_figures()
current_game.populate_board()
current_game.board.output_grid()
