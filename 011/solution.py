#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/sum-of-digits
"""
from typing import List


def sum_of_digits(n: int) -> int:
    go = True
    tmp = n
    sums = 0
    while go:
        tmp /= 10
        n_10 = int(tmp)
        # float issues
        sums += 10*round(tmp - n_10, 1)
        tmp = n_10
        go = n_10 > 0
    return int(sums)


def main() -> None:
    n = int(input())
    result: List[str] = ['']*n
    for i in range(0, n):
        (a, b, c) = list(map(int, input().split(" ")))
        result[i] = str(sum_of_digits(a*b+c))
    print(" ".join(result))


main()
