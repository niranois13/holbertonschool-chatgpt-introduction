#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given integer.

    Arguments:
        n (int): The integer for which factorial is to be calculated.

    Returns:
        int: The factorial of the given integer.
        ValueError: If the input is negative.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
