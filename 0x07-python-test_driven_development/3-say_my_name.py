#!/usr/bin/python3
"""Defines a function that prints first and last name"""


def say_my_name(first_name, last_name):
    """prints first and last name

    Args:
        first_name: The first name
        last_name: The last name
    Raises:
        TypeError: if first and last name are not strings
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string or last_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
