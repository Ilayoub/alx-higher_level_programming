#!/usr/bin/python3
"""The program creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates a Python object"""
    with open(filename) as f:
        return json.load(f)
