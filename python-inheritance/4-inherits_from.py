#!/usr/bin/python3
"""defines the function inherits_from"""

def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class
    (directly or indirectly), otherwise False"""

    return isinstance(obj, a_class) and type(obj) is not a_class
