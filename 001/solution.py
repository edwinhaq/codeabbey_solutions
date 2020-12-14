#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/sum-of-two
"""


def sum_of_two(in_a: int, in_b: int) -> int:
    return in_a + in_b


def main() -> None:
    (a, b) = list(map(int, input().split(" ")))
    print(sum_of_two(a, b))


main()
