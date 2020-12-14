#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/neumanns-random-generator
"""
from typing import List
import math


def get_input_data() -> List[int]:
    _ = int(input())
    return list(map(int, input().split(" ")))


def neumanns_random_generator(initial: int, history: List[int]) -> int:
    if len(history) == 0:
        history.append(initial)
    neumanns = math.floor(initial * initial/100) % 10000
    if neumanns in history:
        return len(history)
    history.append(neumanns)
    return neumanns_random_generator(neumanns, history)


def paint(initial: int) -> str:
    history: List[int] = []
    return str(neumanns_random_generator(initial, history))


def main() -> None:
    print(' '.join(map(paint, get_input_data())))


main()
