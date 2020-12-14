#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/modulo-and-time-difference
"""
from typing import List, Tuple


def days2secs(n: int) -> int:
    return 24*60*60*n


def hours2secs(n: int) -> int:
    return 60*60*n


def minutes2secs(n: int) -> int:
    return 60*n


def modulo_and_time_difference(d1: int, h1: int, m1: int, s1: int,
                               d2: int, h2: int, m2: int, s2: int) -> \
        Tuple[int, int, int, int]:
    t1 = days2secs(d1) + hours2secs(h1) + minutes2secs(m1) + s1
    t2 = days2secs(d2) + hours2secs(h2) + minutes2secs(m2) + s2
    diff = t2 - t1
    s = diff % 60
    diff = int(diff / 60)
    m = diff % 60
    diff = int(diff / 60)
    h = diff % 24
    diff = int(diff / 24)
    return diff, h, m, s


def main() -> None:
    nn = int(input())
    result: List[str] = [""]*nn
    for i in range(0, nn):
        (d1, h1, m1, s1, d2, h2, m2, s2) = tuple(map(int, input().split(" ")))
        diff = modulo_and_time_difference(d1, h1, m1, s1, d2, h2, m2, s2)
        result[i] = "(%s %s %s %s)" % diff
    print(" ".join(result))


main()
