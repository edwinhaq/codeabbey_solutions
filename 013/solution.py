#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/weighted-sum-of-digits
"""
from typing import List


def wsod(a: int) -> int:
    out = 0
    i = 1
    for x in str(a):
        out += i * int(x)
        i += 1
    return out


def main() -> None:
    nn = int(input())
    result: List[str] = [""]*nn
    i = 0
    for inp in list(map(int, input().split(" "))):
        result[i] = str(wsod(inp))
        i += 1
    print(" ".join(result))


main()
