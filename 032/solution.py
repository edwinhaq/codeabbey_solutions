#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/josephus-problem
"""


def josephus(n: int, k: int):
    person_array = list(range(1, n+1))
    i = 1
    go = True
    while go:
        idx_del = []
        for x in range(0, len(person_array)):
            if i % k == 0:
                idx_del.append(x)
            i += 1
        idx_del.reverse()
        for x in idx_del:
            person_array.pop(x)
            if len(person_array) == 1:
                go = False
    return person_array[0]


def main() -> None:
    n, k = tuple(map(int, input().split(" ")))
    print(josephus(n, k))


main()
