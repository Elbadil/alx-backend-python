#!/usr/bin/env python3
"""Defining a function called safe_first_element"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of any type of list if
    the list exists else None"""
    if lst:
        return lst[0]
    else:
        return None
