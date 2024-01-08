#!/usr/bin/env python3
"""
This module contains the asynchronous coroutine wait_n.
"""

import asyncio
from typing import List

# Import the wait_random function using a different approach
import importlib.util

spec = importlib.util.spec_from_file_location(
    "0-basic_async_syntax", "0-basic_async_syntax.py")
wait_random = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    # Create a list to store the delays
    delays = []

    # Use asyncio.gather to run multiple wait_random coroutines concurrently
    coroutines = [wait_random.wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)

    # Sort the results to get delays in ascending order
    delays = sorted(results)

    return delays


if __name__ == "__main__":
    # Example usage
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
