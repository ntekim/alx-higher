#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argc = argc - 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc), end="\n")
        print("{}: {}".format(argc - 1, sys.argv[1]), end="\n")
    else:
        print("{} arguments:".format(argc), end="\n")

    for i in range(int(argc)):
        print("{}: {}".format(i + 1, sys.argv[i + 1]), end="\n")
