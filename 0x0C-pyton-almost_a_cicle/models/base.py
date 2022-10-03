#!/usr/bin/python3
"""The goal of this module is to manage id attribute
    in all your future classes and to avoid duplicating
    the same code (by extension, same bugs)
"""


class Base:
    """The base class of all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#if __name__  == "__main__":
    #Base()
