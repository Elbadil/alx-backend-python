#!/usr/bin/env python3
"""Defining a function called wait_n"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """"""
    counter = 0
    delaysList = []
    while counter < n:
        value = await wait_random(max_delay)
        delaysList.append(value)
        counter += 1
    delaysList.sort()
    return delaysList
