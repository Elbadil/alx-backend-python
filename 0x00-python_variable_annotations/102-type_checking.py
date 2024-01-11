#!/usr/bin/env python3
"""Defining a function called zoom_array"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """returns a list of element in range of factor"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
