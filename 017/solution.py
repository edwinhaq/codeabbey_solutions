#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/array-checksum
"""
from typing import List


def array_checksum(array: List[int]) -> int:
    result = 0
    for i in array:
        result = (i + result) * 113 % 10000007
    return result


def main() -> None:
    _ = int(input())
    array = list(map(int, input().split(" ")))
    result = array_checksum(array)
    print(result)


main()
