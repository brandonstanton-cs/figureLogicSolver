"""
class file for figures, and their various subclasses
a figure that resides on the game board, and starts at a particular index
    e.g. if the game board is of size 10x10, a figure that is 2 from the left, and 2 from the top is at location [2, 2]
a figure can also be of a particular length (e.g. 3 length figure might be: 345)
"""
from characteristics import Characteristic


# base class for a figure, has rudimentary information about the figure, such as value, and length
class Figure:
    def __init__(self, length, origin):
        self.value = 0        # the integer value of the figure
        self.length = length  # the length of the figure
        self.origin = origin  # where the first number resides on the game board
        self.characteristic = Characteristic()

    def figure_length(self):
        return self.length


# TESTING BLOCK:
# test_object = Figure(5, [5, 5])  # test object with a length of five, and an origin point of 5x, 5y
# test_object.characteristic.set_characteristic('fig-product')  # setting the characteristic of the figure to a product
# test_object.characteristic.show_characteristic()  # revealing what characteristic the figure has
# print(test_object.figure_length())


# subclass of Figure, a down figure is placed on the game board differently (top to bottom)
class Down(Figure):
    def __init__(self, length, origin):
        super().__init__(length, origin)
        self.feature = 'down'


# subclass of Figure, an up figure is placed on the game board differently (left to right)
class Across(Figure):
    def __init__(self, length, origin):
        super().__init__(length, origin)
        self.feature = 'across'
