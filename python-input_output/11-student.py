#!/usr/bin/python3
""" Student class module """


class Student:
    """ Defines a student """

    def __init__(self, first_name, last_name, age):
        """ Instantiation with first_name, last_name, and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves dictionary representation of Student """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
