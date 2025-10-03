#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save it to a file.
    """
    try:

        root = ET.Element("data")


        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)


        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file and convert it back to a Python dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()


        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        return dictionary
    except FileNotFoundError:
        return None
    except Exception:
        return None
