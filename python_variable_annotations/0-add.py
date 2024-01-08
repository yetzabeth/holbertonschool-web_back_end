#!/usr/bin/env python3
"""
This module contains the function add.
"""


def add(a: float, b: float) -> float:
    """
    Adds two floats and returns their sum.

    Args:
        a (float): The first float.
        b (float): The second float.

    Returns:
        float: The sum of a and b.
    """
    return a + b


if __name__ == "__main__":
    # Test the function
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
