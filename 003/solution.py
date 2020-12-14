#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/sums-in-loop
"""
from typing import List


def sums_in_loop(n: int, array1: list, array2: list):
    accum: List[int] = [0]*n
    for i in range(0, n):
        accum[i] = array1[i] + array2[i]
    return accum


def main() -> None:
    n = int(input())
    array1: List[int] = [0]*n
    array2: List[int] = [0]*n
    for i in range(0, n):
        (array1[i], array2[i]) = list(map(int, input().split(" ")))
    print(" ".join(list(map(str, sums_in_loop(n, array1, array2)))))


main()
