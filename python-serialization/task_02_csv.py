#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""


import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into a JSON file named data.json.

    Args:
        csv_filename (str): The name of the CSV file.

    Returns:
        bool: True if successful, False if an error occurred.
    """
    try:

        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

      
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False
