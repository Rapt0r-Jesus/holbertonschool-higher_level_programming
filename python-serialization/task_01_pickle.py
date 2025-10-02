#!/usr/bin/env python3
"""serialize and deserialize custom Python objects using the pickle module"""


import pickle


class CustomObject:
    """a class for an object"""

    def __init__(self, name: str, age: int, is_student: bool):
        """a constructor"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the object and save it to a file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize from file and return a CustomObject instance"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except Exception:
            return None
