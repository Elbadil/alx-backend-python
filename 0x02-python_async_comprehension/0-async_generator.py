#!/usr/bin/env python3
"""Defining a coroutine called async_generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """waits 1 second after each iteration and yields
    a randum number"""
    for _ in range(10):
        await asyncio.sleep(1)
        # transforms the function into an iterator
        yield random.uniform(0, 10)
