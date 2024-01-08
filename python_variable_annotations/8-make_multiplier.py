#!/usr/bin/env python3
"""
This module contains the function make_multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function.

    Returns:
        Callable[[float], float]: A function that multiplies a float
        by the specified multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the specified multiplier.

        Args:
            x (float): The input float.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function


if __name__ == "__main__":
    # Test the function
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
