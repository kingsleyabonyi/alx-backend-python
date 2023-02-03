#!/usr/bin/env python3

'''Returns the sum of interger and float as  float
'''

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int,float]]) -> float:
    return float(sum(mxd_lst))