#!/usr/bin/env python3
"""Defining a courotine called async_generator"""
import asyncio
import random


async def async_generator():
    """waits 1 second after each iteration and yields
    a randum number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
