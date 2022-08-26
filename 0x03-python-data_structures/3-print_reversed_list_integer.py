#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    real_len = length - 1
    for i in range(length):
        print("{}".format(my_list[real_len - i]))
