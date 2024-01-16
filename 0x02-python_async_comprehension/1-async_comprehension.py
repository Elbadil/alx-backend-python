#!/usr/bin/env python3
"""Defining a coroutine called async_comprehension"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects 10 random numbers using an async
    comprehensing over async_generator then returns
    a list of the 10 random numbers"""
    results = [i async for i in async_generator()]
    return results
