#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/array-counters
"""
from typing import List


def array_counters(array: List[int]):
    out = [0]*(max(array)+1)
    for i in array:
        out[i] += 1
    return out[1:]


def main() -> None:
    m, n = tuple(map(int, input().split(" ")))
    array = list(map(int, input().split(" ")))
    print(" ".join(map(str, array_counters(array))))
    

main()
