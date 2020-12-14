#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/min-of-three
"""
from typing import List


def min_of_three(n: int, array1: List[int], array2: List[int],
                 array3: List[int]):
    mins: List[int] = [0]*n
    for i in range(0, n):
        x = array1[i] if array1[i] < array2[i] else array2[i]
        mins[i] = x if x < array3[i] else array3[i]
    return mins 


def main() -> None:
    n = int(input())
    array1: List[int] = [0]*n
    array2: List[int] = [0]*n
    array3: List[int] = [0]*n
    for i in range(0, n):
        (array1[i], array2[i], array3[i]) = list(map(int, input().split(" ")))
    print(" ".join(list(map(str, min_of_three(n, array1, array2, array3)))))


main()
