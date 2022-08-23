#!/usr/bin/python3
#write a program that prints the ASCII alphabet
#in lowercase
def lowercaseAlphabets():
    for c in range(97, 123):
        if c == 'q' or c == 'e':
            continue;
        print(chr(c), end = " ");

lowercaseAlphabets()
