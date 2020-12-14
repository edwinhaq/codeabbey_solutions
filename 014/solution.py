#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/modular-calculator
"""


def modular_calculator(n: int, op: str, m: int) -> int:
    out = 0
    if op == "+":
        out = n + m
    if op == "*":
        out = n * m
    if op == "%":
        out = n % m
    return out 


def main() -> None:
    n = int(input())
    go = True
    while go:
        (op, m) = input().split(" ")
        n = modular_calculator(n, op, int(m))
        if op == "%":
            go = False
    print(n)


main()
