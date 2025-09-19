#!/usr/bin/python3
"""Printing a square"""


class Square:
    """A square is a geometrical form"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
    
    def my_print(self):
        """Print the square with the character # to stdout."""
        if self.__size == 0:
            print()  # Empty line if size is 0
            return
        for _ in range(self.__size):
            print("#" * self.__size)
