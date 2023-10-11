#!/usr/bin/python3
"""The program returns an object (Python data structure)
   represented by a JSON string"""
import json


def from_json_string(my_str):
    """Returns the Python object representation of a JSON string"""
    return json.loads(my_str)
