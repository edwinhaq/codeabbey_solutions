#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/rounding
"""
from typing import List


def rounding(n: int, array1: List[int], array2: List[int]) -> List[int]:
    rounds: List[int] = [0]*n
    for i in range(0, n):
        div = array1[i] / array2[i]
        unit = div / abs(div)
        frac = abs(div - int(div))
        div = int(div) if frac < 0.5 else int(div)+unit
        rounds[i] = int(div)
    return rounds


def main() -> None:
    n = int(input())
    array1: List[int] = [0]*n
    array2: List[int] = [0]*n
    for i in range(0, n):
        (array1[i], array2[i]) = list(map(int, input().split(" ")))
    print(" ".join(list(map(str, rounding(n, array1, array2)))))


main()
