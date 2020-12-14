#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/vowel-count
"""


def vowel_count(line: str) -> int:
    return len([x for x in line if x in "aouiey"])


def main() -> None:
    n = int(input())
    result = [0]*n
    for i in range(0, n):
        result[i] = vowel_count(input())
    print(" ".join(map(str, result)))


main()
