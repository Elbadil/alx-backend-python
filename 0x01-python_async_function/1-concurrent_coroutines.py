#!/usr/bin/env python3
"""Defining a function called wait_n"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays in ascending order"""
    tasks = [(wait_random(max_delay)) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    sorted_results = sorted(results)
    return sorted_results
