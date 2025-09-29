#!/usr/bin/python3
"""Append a string at the end of a UTF8 text file
 and return number of characters added"""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file and return
    number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
