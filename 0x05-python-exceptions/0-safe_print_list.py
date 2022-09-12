#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
        Program prints x elements of a list

    Args:
        my_list - list to work with
        x - number of elements to print
    """

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except Exception:
        print()
        return i
