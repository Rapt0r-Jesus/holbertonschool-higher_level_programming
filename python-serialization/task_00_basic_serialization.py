#!/usr/bin/env python3
"""Create a basic serialization module that adds
 the functionality to serialize a Python dictionary
  to a JSON file and deserialize the JSON file to 
  recreate the Python Dictionary. """

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    Args:
        data (dict): The dictionary to serialize.
        filename (str): The JSON file to save to. Overwrites if it exists.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.
    Args:
        filename (str): The JSON file to read from.
    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
