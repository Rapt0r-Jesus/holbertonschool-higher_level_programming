#!/usr/bin/python3
"""
Defines a Square class inheriting from BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of square"""
        return self.__size ** 2
