#!/usr/bin/python3
# Function to print the alphabet
# in lower case
def lowercaseAlphabets():
    # lowercase
    for c in range(97, 123):
        print("{}".format(chr(c)), end = "");

lowercaseAlphabets()
