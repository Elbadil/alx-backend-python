#!/usr/bin/env python3
"""Defining a function called element_length"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples of sequence and integers"""
    return [(i, len(i)) for i in lst]
