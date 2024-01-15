#!/usr/bin/env python3
"""Defining a function wait_random"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random delay between 0 and max_delay
    and returns the timer of the delay"""
    timer = random.uniform(0, max_delay)
    await asyncio.sleep(timer)
    return timer
