#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/linear-congruential-generator
"""


def linear_congruential_generator(a: int, c: int, m: int, x: int, n: int) -> int:
    out = (a * x + c) % m
    if n <= 1:
        return out
    else:
        return linear_congruential_generator(a, c, m, out, n - 1)


def main() -> None:
    nn = int(input())
    result = [""]*nn
    for i in range(0, nn):
        a, c, m, x, n = tuple(map(int, input().split(" ")))
        result[i] = str(linear_congruential_generator(a, c, m, x, n))
    print(" ".join(result))


main()
