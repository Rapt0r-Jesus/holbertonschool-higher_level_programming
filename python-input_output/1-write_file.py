#!/usr/bin/python3
"""Write a string to a UTF8 text file and return number of characters written"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
