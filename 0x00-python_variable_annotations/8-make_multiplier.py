#!/usr/bin/env python3
"""Defining a function called make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float as argument and returns a function that
    multiplies a float by multiplier"""
    def more_multiplying(multiplier2: float):
        """return multiplier from the make_multiplier function multiplied
        by the second given multiplier"""
        return multiplier * multiplier2
    return more_multiplying
