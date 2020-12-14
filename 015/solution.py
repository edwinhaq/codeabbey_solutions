#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/maximum-of-array
"""
import sys
from typing import List, Tuple


def maximum_of_array(array: List[int]) -> Tuple[int, int]:
    nmax = -sys.maxsize+1
    nmin = sys.maxsize
    for x in array:
        if x < nmin:
            nmin = x
        if x > nmax:
            nmax = x
    return nmax, nmin


def main() -> None:
    data = list(map(int, input().split(" ")))
    result = list(map(str, maximum_of_array(data)))
    print(" ".join(result))


main()
