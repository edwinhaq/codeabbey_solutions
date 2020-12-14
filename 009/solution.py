#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/triangles
"""
from typing import List


def triangles(a: int, b: int, c: int) -> int:
    nmax = max([a, b, c])
    nsum = sum([a, b, c])
    return 0 if nmax > nsum - nmax else 1


def main() -> None:
    n = int(input())
    result: List[str] = ['']*n
    for i in range(0, n):
        (a, b, c) = list(map(int, input().split(" ")))
        result[i] = str(triangles(a, b, c))
    print(" ".join(result))


main()
