#!/usr/bin/env python3
"""
This module contains the asynchronous coroutine wait_random.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds.

    Args:
        max_delay (int): The maximum delay for the random sleep.

    Returns:
        float: The random delay.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
