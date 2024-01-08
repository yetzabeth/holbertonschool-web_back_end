#!/usr/bin/env python3
"""
This module contains the function floor.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    Args:
        n (float): The input float.

    Returns:
        int: The floor of the input float.
    """
    return math.floor(n)


if __name__ == "__main__":
    # Test the function
    ans = floor(3.14)
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
