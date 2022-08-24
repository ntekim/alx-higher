#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last_digit(num):
    num = num % 10
    if num < -9 and num > 9:
        last_digit(num)
    else:
        if num > 5 and num >= 6:
            print("Last digit of {} is {} and is greater than 5".format(number, num))
        elif num < 6 and num != 0:
            print("Last digit of {} is {} and less than 6 and not 0".format(number, num))
        elif num == 0:
            print("Last digit of {} is {} and is 0".format(number, num))


last_digit(number)
