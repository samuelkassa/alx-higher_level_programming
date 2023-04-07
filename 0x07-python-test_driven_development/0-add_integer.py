#!/usr/bin/python3
"""Defines integer addition function"""


def add_integer(a, b=98):
    """Return the integer addition of a and b

    Float arguments are typecasted to ints before addition is perfomed

    Raises:
        TypeError: if either a or b is non-integer or non-float
    """
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
