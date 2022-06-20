"""
class file for figure characteristics
figure characteristics define what methods need to be employed to solve for the value of a figure
they can range from simple arithmetic, to logic-based methods
"""
# TODO maybe represent this list as an enum??
characteristic_list = ['fig-product', 'fig-sum', 'fig-diff', 'fig-divide', 'fig-rep', 'dig-rep', 'reverse']


class Characteristic:
    def __init__(self):
        self.characteristic = ''

    def set_characteristic(self, characteristic):
        if characteristic_list.__contains__(characteristic):
            self.characteristic = characteristic

    def show_characteristic(self):
        print(self.characteristic)


# TESTING BLOCK:
# test_object = Characteristic()
# test_object.set_characteristic('fig-product')
# test_object.show_characteristic()


# TODO create and name all possible characteristics based off of puzzles from books

""" ARITHMETIC BASED CHARACTERISTICS"""


def figure_product(first_figure, second_figure):
    print("Hi")


def figure_sum(first_figure, second_figure):
    print("Hi")


def figure_difference(first_figure, second_figure):
    print("Hi")


def figure_division(first_figure, second_figure):
    print("Hi")


""" LOGIC BASED CHARACTERISTICS"""


def figure_repeat(figure):
    print("Hi")


def digit_repeat(digit='0'):
    print("Hi")


def reverse(figure):
    print("Hi")


