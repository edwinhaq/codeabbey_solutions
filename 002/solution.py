#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/sum-in-loop
"""
from typing import List


def sum_in_loop(array: List[int]) -> int:
    accum: int = 0
    for i in array:
        accum += i
    return accum


def main() -> None:
    _ = input()
    print(sum_in_loop(list(map(int, input().split(" ")))))


main()
