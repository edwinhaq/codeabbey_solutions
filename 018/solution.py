#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/square-root
"""
import math


def square_root(x: int, n: int):
    r = 1
    for i in range(0, n):
        d = x / r 
        absd = abs(r - d)
        r = (r + d) / 2
        if absd <= 1e-7:
            break
    out = round(r, 7)
    dec, _ = math.modf(out)
    if dec == 0:
        out = int(out)
    return out


def main() -> None:
    n = int(input())
    result = [""]*n
    for i in range(0, n):
        (x, n) = tuple(map(int, input().split(" ")))
        result[i] = str(square_root(x, n))
    print(" ".join(result))


main()
