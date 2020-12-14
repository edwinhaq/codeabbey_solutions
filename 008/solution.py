#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/arithmetic-progression
"""
from typing import List


def arithmetic_progression(a: int, b: int, n: int) -> int:
    prog: int = 0
    for i in range(0, n):
        prog += a + b * i
    return prog 


def main() -> None:
    nn = int(input())
    result: List[str] = ['']*nn
    for i in range(0, nn):
        (a, b, n) = list(map(int, input().split(" ")))
        result[i] = str(arithmetic_progression(a, b, n))
    print(" ".join(result))


main()
