#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/fahrenheit-celsius
"""
from typing import List


def f2c(f: int) -> int:
    m = 100/(212-32)
    b = -32 * m
    return int(round(m*f + b))


def fahrenheit_celsius(fahrenheit: List[int]) -> List[int]:
    n: int = len(fahrenheit)
    celsius: List[int] = [0]*n
    for i in range(0, n):
        celsius[i] = f2c(fahrenheit[i])
    return celsius


def main() -> None:
    data = list(map(int, input().split(" ")))
    print(" ".join(list(map(str, fahrenheit_celsius(data[1:])))))


main()
