#!/usr/bin/env python3
"""Defining a function task_wait_n"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calling task_wait_random instead of wait_random"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    sorted_results = sorted(results)
    return sorted_results
