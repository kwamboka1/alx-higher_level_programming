#!/usr/bin/python3
""" Module that returns the dictionary description with a simple
data structure for a JSON serialization of an object
"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    resc = {}
    if hasattr(obj, "__dict__"):
        resc = obj.__dict__.copy()
    return resc
