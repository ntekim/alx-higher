#!/usr/bin/python3
def uniq_add(my_list=[]):

    # initialize a null list
    unique_list = []
    total = 0
    # traverse for all elements
    for x in my_list:
        # check if exists in unique_list or not
        if x not in unique_list:
            total += x
            unique_list.append(x)
    return total
