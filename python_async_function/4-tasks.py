#!/usr/bin/env python3
"""
This module contains the function task_wait_n.
"""

import asyncio
from typing import List, Generator

# Import the wait_random and task_wait_random functions using a different approach
import importlib.util

spec = importlib.util.spec_from_file_location(
    "1-concurrent_coroutines", "1-concurrent_coroutines.py")
wait_random = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random)

spec = importlib.util.spec_from_file_location("3-tasks", "3-tasks.py")
task_wait_random = importlib.util.module_from_spec(spec)
spec.loader.exec_module(task_wait_random)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay for each task_wait_random.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    # Use asyncio.gather to run multiple task_wait_random coroutines concurrently
    coroutines = [task_wait_random.task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*coroutines)

    # Sort the results to get delays in ascending order
    delays = sorted(results)

    return delays


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
