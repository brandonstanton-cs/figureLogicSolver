"""
class file for figures
a figure that resides on the game board, and starts at a particular index
    e.g. if the game board is of size 10x10, a figure that is 2 from the left, and 2 from the top is at location [2, 2]
a figure can also be of a particular length (e.g. 3 length figure might be: 345)
"""
from characteristics import Characteristic


# base class for a figure, has rudimentary information about the figure, such as value, and length
class Figure:
    def __init__(self, length, x_origin, y_origin, if_across=True):
        self.value = 0        # the integer value of the figure
        self.length = length  # the length of the figure
        self.origin = [x_origin, y_origin]  # where the first number resides on the game board
        self.characteristic = Characteristic()
        self.is_across = if_across

    def describe_figure(self):
        print("Figure details:")
        print("origin: " + str(self.origin) + ", length: " + str(self.length) + ", is across?: " + str(self.is_across))