#!/usr/bin/env python3
"""
This module contains the function sum_list.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of the elements in the input list.

    Args:
        input_list (List[float]): The list of floats.

    Returns:
        float: The sum of the elements in the input list.
    """
    return sum(input_list)
