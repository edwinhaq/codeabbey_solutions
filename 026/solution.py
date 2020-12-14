#!/usr/bin/env python3
"""
https://www.codeabbey.com/index/task_view/greatest-common-divisor
"""


def gcd(n: int, m: int) -> int:
    nmax = max(n, m)
    nmin = min(n, m)
    nmod = nmax % nmin
    if nmod == 0:
        return nmin
    else:
        return gcd(nmin, nmod)


# def lcm(n: int, m: int):
#    return n * m / gcd(n, m)


def outformat(n: int, m: int) -> str:
    gd = gcd(n, m)
    ld = int(n * m / gd)
    return "(%s %s)" % (gd, ld)


def main() -> None:
    nn = int(input())
    result = [""]*nn
    for i in range(0, nn):
        n, m = tuple(map(int, input().split(" ")))
        result[i] = outformat(n, m)
    print(" ".join(result))


main()
