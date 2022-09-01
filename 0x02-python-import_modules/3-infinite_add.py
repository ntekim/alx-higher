#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    num = 0

    for i in range(1, argc):
        num += int(sys.argv[1])
    print("{}".format(num))
