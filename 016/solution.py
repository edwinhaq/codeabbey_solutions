#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/average-of-array
"""
from typing import List


def average_of_array(array: List[int]) -> int:
    return round(sum(array)/len(array))


def main() -> None:
    n = int(input())
    result = [""]*n
    for i in range(0, n):
        array = list(map(int, input().split(" ")))
        result[i] = str(average_of_array(array[:-1]))
    print(" ".join(result))


main()
