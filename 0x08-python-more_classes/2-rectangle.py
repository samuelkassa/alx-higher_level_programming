#!/usr/bin/python3
"""
    Defines a Rectangle class
"""


class Rectangle:
    """
    Represent a Rectangle
    """
    
    def __init__(self, width = 0, height = 0):
        """Initialize a new Rectangle.
        Args:
            width(int):  the width of the Rectangle
            height(int): the height of the Rectangle
        """
        self.width = width
        self.height = height
   
   """
   property
   """
   @property
   def width(self):
       return self.__width

   """
   setter
   """
   @width.setter
   def width(self, value):
       if not isinstance(value, int):
           raise TypeError("width must be an integer")
       if value < 0:
           raise ValueError("width must be >= 0")
       self.__width = value

    """
    propety for height attribute
    """
    @property
    def height(self):
        return self.__height

    """
    height setter
    """
    @height.setter
    def height(self, height):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """ public instance method for calculating the area
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """
        Public instance method for calculating the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
