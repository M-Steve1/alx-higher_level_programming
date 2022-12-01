#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calculator():
    argv_len = len(sys.argv)
    operators = ["+", "-", "*", "/"]
    result = 0

    if argv_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif argv_len == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] not in operators:
            print("Unknown operator. Available"
                  " operators: +, -, * and /")
            sys.exit(1)
        elif sys.argv[2] == "+":
            result = add(a, b)
        elif sys.argv[2] == "-":
            result = sub(a, b)
        elif sys.argv[2] == "*":
            result = mul(a, b)
        elif sys.argv[2] == "/":
            result = div(a, b)

    print("{} {} {} = {}".format(a, sys.argv[2], b, result))


if __name__ == '__main__':
    calculator()
