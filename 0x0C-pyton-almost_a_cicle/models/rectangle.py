#!/usr/bin/python3
"""Defines a Rectangle that inherits the Base class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
            x (int): Yet to figure it out
            y (int): yet to figure out its use
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Get/set the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        #if value <= 0:
            #raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x - assign value to x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return x"""
        return self.__x

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)


