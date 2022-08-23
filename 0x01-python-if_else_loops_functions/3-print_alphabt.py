#!/usr/bin/python3
#write a program that prints the ASCII alphabet
#in lowercase
def lowercaseAlphabets():
    for c in range(97, 123):
        if chr(c) == 'e':
            continue;
        elif chr(c) == 'q':
            continue;
        print("{}".format(chr(c)), end = " ");


lowercaseAlphabets()
