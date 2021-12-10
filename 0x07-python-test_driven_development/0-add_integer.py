#!/usr/bin/python3
"""

This Module is composed of a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers

    Args are:
        a: first number
        b: second number

    Returns:
        The addition of the two given numbers(a + b)

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer ")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    """Convert a and b into integers"""
    a = int(a)
    b = int(b)
    return (a + b)
