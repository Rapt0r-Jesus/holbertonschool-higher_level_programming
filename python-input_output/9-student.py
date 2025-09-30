#!/usr/bin/python3
"""
    Defines a student with first name, last name, and age.
    """

    
class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of a Student instance
        suitable for JSON serialization.
        """
        return self.__dict__
