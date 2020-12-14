#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/matching-brackets
"""
from typing import List


def check_open_close(open_char: str, close_char: str) -> bool:
    check = {'(': ')', '[': ']', '{': '}', '<': '>'}
    out = open_char in check and check[open_char] == close_char
    return out


def matching_brackets(line: str) -> int:
    # ()[]{}<>
    get_close_with_open = {'(': ')', '[': ']', '{': '}', '<': '>'}
    get_open_with_close = {')': '(', ']': '[', '}': '{', '>': '<'}
    opens = list(get_close_with_open.keys())
    closes = list(get_open_with_close.keys())
    lifo = []
    for x in line:
        if x in opens:
            lifo.append(x)
        for c in closes:
            if x != c:
                continue
            if len(lifo) > 0:
                y = lifo.pop()
                if not check_open_close(y, x):
                    return 0
            else:
                return 0
    return 1 if len(lifo) == 0 else 0


def get_input_data() -> List[str]:
    n = int(input())
    result: List[str] = []
    for _ in range(0, n):
        result.append(input())
    return result


def main() -> None:
    result: List[str] = []
    for line in get_input_data():
        result.append(str(matching_brackets(line)))
    print(" ".join(result))


main()
