#!/usr/bin/env python3
"""
This module contains the function task_wait_random.
"""

import asyncio
from typing import Generator

# Import the wait_random function using a different approach
import importlib.util

spec = importlib.util.spec_from_file_location(
    "0-basic_async_syntax", "0-basic_async_syntax.py")
wait_random = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wait_random)


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random function.

    Args:
        max_delay (int): The maximum delay for wait_random.

    Returns:
        asyncio.Task: The asyncio task for wait_random.
    """
    # Create a coroutine generator using the regular function syntax
    async def wait_random_coroutine(max_delay: int) -> float:
        return await wait_random.wait_random(max_delay)

    # Create a task from the coroutine generator
    task = asyncio.ensure_future(wait_random_coroutine(max_delay))
    return task


if __name__ == "__main__":
    # Example usage
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))
