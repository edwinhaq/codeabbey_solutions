#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/bubble-in-array
"""

from typing import List, Tuple


def get_input_data() -> List[int]:
    result: List[int] = list(map(int, input().split(" ")))
    return result


def swap(array: List[int], pos1: int, pos2: int) -> None:
    tmp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = tmp


def bubble_in_array(array: List[int], pos: int, n_swaps: int = 0) \
        -> Tuple[int, List[int]]:
    if array[pos] == -1:
        return n_swaps, array
    if array[pos] < array[pos - 1]:
        swap(array, pos, pos - 1)
        n_swaps += 1
    return bubble_in_array(array, pos + 1, n_swaps)


def array_checksum(array: List[int], pos: int = 0, checksum: int = 0) -> int:
    if pos == len(array):
        return checksum
    checksum = (array[pos] + checksum) * 113 % 10000007
    return array_checksum(array, pos + 1, checksum)


def main() -> None:
    input_array = get_input_data()
    swaps, array = bubble_in_array(input_array, 1)
    print(swaps, array_checksum(array[:-1]))


main()

# cat ./DATA.lst | ./edwinhaq.py
# 33 2036273
