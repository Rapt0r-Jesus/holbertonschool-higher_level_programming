#!/usr/bin/python3
""" a class MyList that inherits from list"""


class MyList(list):
    """
    MyList extends the built-in list with a method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
