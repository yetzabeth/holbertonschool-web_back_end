#!/usr/bin/env python3
"""
This module contains the function element_length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains
    an element from the input
    iterable 'lst' and its length.

    Args:
        lst (Iterable[Sequence]): The input iterable.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples
        containing elements and their lengths.
    """
    return [(i, len(i)) for i in lst]


if __name__ == "__main__":
    # Test the function
    print(element_length.__annotations__)
