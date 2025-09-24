#!/usr/bin/python3
"""
Defines a Rectangle class inheriting from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create a class rectangle"""

    def __init__(self, width, height):
        """Initialize rectangle with width and height, both validated"""
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
