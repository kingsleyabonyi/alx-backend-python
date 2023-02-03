#!/usr/bin/env python3

'''Annotate the below function’s parameters and return values with the appropriate types
'''

from typing import List, Sequence, Iterable, Turple 

def element_length(lst: Iterable(Sequence)) -> List[Turple[Sequence, int]]:
    return [(i, len(i)) for i in lst]