#!/usr/bin/env python3
"""
This module contains the function to_kv.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k and the square of the int/float v.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input integer or float.

    Returns:
        Tuple[str, float]: A tuple containing the string k and the square of v.
    """
    return k, v ** 2


if __name__ == "__main__":
    # Test the function
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
