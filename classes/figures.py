

"""
class file for figures, and their various subclasses
a figure that resides on the game board, and starts at a particular index
    e.g. if the game board is of size 10x10, a figure that is 2 from the left, and 2 from the top is at location [2, 2]
a figure can also be of a particular length (e.g. 3 length figure might be: 345)
"""


# base class for a figure, has rudimentary information about the figure, such as value, and length
class Figure:
    def __init__(self, length, origin):
        self.value = 0        # the integer value of the figure
        self.length = length  # the length of the figure
        self.origin = origin  # where the first number resides on the game board
        self.characteristic = None

    # associates a characteristic to solve the value of the figure with other figures!
    def set_characteristic(self, characteristic):
        self.characteristic = characteristic

    def select_characteristic(self):
        print("Select Characteristic")
        print(self.value)
        # TODO create map of associations that can be made between figures, e.g. 'Sum', 'Multiple', etc.


# subclass of Figure, a down figure has a different method for determining its adjoining squares on the game board
class Down(Figure):
    def __init__(self, length, origin):
        super().__init__(length, origin)


# subclass of Figure, an up figure has a different method for determining its adjoining squares on the game board
class Across(Figure):
    def __init__(self, length, origin):
        super().__init__(length, origin)
