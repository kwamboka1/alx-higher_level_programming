#!/usr/bin/python3
"""Class that inherits the attributes references of class list
    Args:
        list: class list
"""


class MyList(list):
    """ Method that prints the sorted list """
    def print_sorted(self):
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
