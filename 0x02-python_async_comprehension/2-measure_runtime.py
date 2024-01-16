#!/usr/bin/env python3
"""Defining a coroutine called measure_runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures total runtime and returns it"""
    start_time = time.time()
    routines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*routines)
    full_time = time.time() - start_time
    return full_time
