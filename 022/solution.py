#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/two-printers
"""
from typing import List, Tuple
import math


def two_printers(x: int, y: int, n: int) -> int:
    ma = max(x, y)
    mi = min(x, y)
    if ma % mi == 0:
        b = int(ma / mi)
        return math.ceil(n*mi*b/(1+b))
    fast = mi * n
    t = fast
    if ma < fast:
        c = 0
        go = True
        while go:
            tmi = fast - c*mi
            tma = c * ma
            if max(tmi, tma) <= t:
                t = max(tmi, tma)
            else:
                go = False
            c += 1
    return t


def get_input_data() -> List[Tuple]:
    n = int(input())
    result: List[Tuple] = []
    for _ in range(0, n):
        # (x, y, n)
        result.append(tuple(map(lambda i: int(i), input().split(" "))))
    return result


def main() -> None:
    result: List[str] = []
    for (x, y, n) in get_input_data():
        result.append(str(two_printers(x, y, n)))
    print(" ".join(result))


main()
