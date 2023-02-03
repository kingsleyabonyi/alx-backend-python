#!/usr/bin/env python3

'''Takes a string, int or float as arguments and returns a turple
'''

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> tuple:
    return (str(k), float(v*2))