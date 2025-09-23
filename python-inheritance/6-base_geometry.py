#!/usr/bin/python3
"""Create a class BaseGeometry with an area method"""


class BaseGeometry:
    """BaseGeometry class with an area method that is not implemented."""

    def area(self):
        """Exception: Always, since area() is not implemented"""
        
        raise Exception("area() is not implemented")
