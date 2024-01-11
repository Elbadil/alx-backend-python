#!/usr/bin/env python3
"""Defining a function called to_kv"""
from typing import Union, Tuple
from math import sqrt


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple where the first element is the str k
    and the second element is v as a float"""
    aTuple = (k, (v * v))
    return aTuple
