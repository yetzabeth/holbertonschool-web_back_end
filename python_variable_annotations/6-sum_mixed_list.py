#!/usr/bin/env python3
"""
This module contains the function sum_mixed_list.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of the elements in the mixed list.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and floats.

    Returns:
        float: The sum of the elements in the mixed list.
    """
    return sum(mxd_lst)
