#!/usr/bin/env python3
"""Defining a function called wait_n"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays in ascending order"""
    delays = [wait_random(max_delay) for _ in range(n)]
    values = await asyncio.gather(*delays)
    values.sort()
    return values
