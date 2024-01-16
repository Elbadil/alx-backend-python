#!/usr/bin/env python3
"""Defining a courotine called async_generator"""
import asyncio
import random


async def async_generator():
    """"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield(random.uniform(0, 10))
