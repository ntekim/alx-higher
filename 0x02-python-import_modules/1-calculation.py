#!/usr/bin/python3
import calculator_1

def calculate():
    """Calculation program

        Returns:
            Prints the result of each calculation as a string
    """
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)), end="\n")
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)), end="\n")
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)), end="\n")
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)), end="\n")

calculate()

if _name_ == "_1-calculation_"
