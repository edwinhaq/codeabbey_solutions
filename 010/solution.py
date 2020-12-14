#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/linear-function
"""
from typing import List, Tuple


def linear_function(x1: int, y1: int, x2: int, y2: int) -> Tuple[int, int]:
    a = int((y2 - y1)/(x2 - x1))
    b = int(y2 - a * x2)
    return a, b


def main() -> None:
    n = int(input())
    result: List[str] = ['']*n
    for i in range(0, n):
        (x1, y1, x2, y2) = list(map(int, input().split(" ")))
        result[i] = "(%s %s)" % linear_function(x1, y1, x2, y2)
    print(" ".join(result))


main()
