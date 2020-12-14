#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/min-of-two
"""
from typing import List


def min_of_two(n: int, array1: List[int], array2: List[int]) -> List[int]:
    mins: List[int] = [0]*n
    for i in range(0, n):
        mins[i] = array1[i] if array1[i] < array2[i] else array2[i]
    return mins 


def main() -> None:
    n = int(input())
    array1: List[int] = [0]*n
    array2: List[int] = [0]*n
    for i in range(0, n):
        (array1[i], array2[i]) = list(map(int, input().split(" ")))
    print(" ".join(list(map(str, min_of_two(n, array1, array2)))))


main()
