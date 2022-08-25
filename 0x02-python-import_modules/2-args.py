#!/usr/bin/python3
import sys


def arguments():
    """Prints number and lists of arguments"""

    argc = len(argv)
    argc = argc - 1

    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc), end="\n")
        print("{}: {}".format(argc - 1, sys.argv[1]), end="\n")
    elif argc > 1:
        print("{} arguments:".format(argc), end="\n")
        for i in range(int(argc)):
            print("{}: {}".format(i + 1, sys.argv[i + 1]), end="\n")


arguments()
