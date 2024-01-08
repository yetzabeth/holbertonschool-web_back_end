#!/usr/bin/env python3
"""
This module contains the function measure_time.
"""

from typing import List
import time
import asyncio

# Import the wait_n function using a different approach
import importlib.util

spec = importlib.util.spec_from_file_location(
    "1-concurrent_coroutines", "1-concurrent_coroutines.py")
wait_n = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_n)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): The number of times to run wait_n.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        float: The average execution time per run.
    """
    start_time = time.time()

    # Use asyncio.run() to measure the total execution time for wait_n
    asyncio.run(wait_n.wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate and return the average execution time per run
    return total_time / n


if __name__ == "__main__":
    # Example usage
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
