#!/usr/bin/python3
"""Python class for a square with private instance fields"""


class Square:
    """Python class for instantiate square"""

    def __init__(self, size):
        """Initialize the class
        Args
         size(int): the size of the square
         """
        self.__size = size
