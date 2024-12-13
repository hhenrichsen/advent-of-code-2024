from functools import cache
from typing import Tuple
import sys

sys.setrecursionlimit(10**6)


@cache
def tokens_rec(
    a: Tuple[int, int],
    a_cost: int,
    b: Tuple[int, int],
    b_cost: int,
    prize: Tuple[int, int],
):
    if prize[0] < 0 or prize[1] < 0:
        return float("inf")
    if prize == (0, 0):
        return 0
    ta = (prize[0] - a[0], prize[1] - a[1])
    tb = (prize[0] - b[0], prize[1] - b[1])
    return min(
        tokens_rec(a, a_cost, b, b_cost, ta) + a_cost,
        tokens_rec(a, a_cost, b, b_cost, tb) + b_cost,
    )


def tokens_linalg(
    a: Tuple[int, int],
    a_cost: int,
    b: Tuple[int, int],
    b_cost: int,
    prize: Tuple[int, int],
) -> int:
    ax, ay = a
    bx, by = b
    px, py = prize
    count_a = (px * by - py * bx) / (ax * by - ay * bx)
    count_b = (px * ay - py * ax) / (bx * ay - by * ax)
    if count_a % 1 != 0 or count_b % 1 != 0:
        return float("inf")
    return int(a_cost * count_a + b_cost * count_b)


def part1(inp: list[str]):
    result = 0
    mode = 0
    ax, ay = None, None
    bx, by = None, None
    px, py = None, None
    ca, cb = 3, 1
    for line in inp:
        if len(line) == 0:
            t = tokens_linalg((ax, ay), ca, (bx, by), cb, (px, py))
            result += t if t != float("inf") else 0
            mode = 0
            continue
        if mode == 0:
            _, n1r, n2r = line.split("+")
            ax = int(n1r[: n1r.index(",")])
            ay = int(n2r)
            mode += 1
            continue
        if mode == 1:
            _, n1r, n2r = line.split("+")
            bx = int(n1r[: n1r.index(",")])
            by = int(n2r)
            mode += 1
            continue
        if mode == 2:
            _, pxr, pyr = line.split("=")
            px = int(pxr[: pxr.index(",")])
            py = int(pyr)
            mode += 1
            continue

    t = tokens_linalg((ax, ay), ca, (bx, by), cb, (px, py))
    result += t if t != float("inf") else 0
    return result


def part2(inp):
    result = 0
    mode = 0
    ax, ay = None, None
    bx, by = None, None
    px, py = None, None
    ca, cb = 3, 1
    for line in inp:
        if len(line) == 0:
            t = tokens_linalg((ax, ay), ca, (bx, by), cb, (px, py))
            result += t if t != float("inf") else 0
            mode = 0
            continue
        if mode == 0:
            _, n1r, n2r = line.split("+")
            ax = int(n1r[: n1r.index(",")])
            ay = int(n2r)
            mode += 1
            continue
        if mode == 1:
            _, n1r, n2r = line.split("+")
            bx = int(n1r[: n1r.index(",")])
            by = int(n2r)
            mode += 1
            continue
        if mode == 2:
            _, pxr, pyr = line.split("=")
            px = int(pxr[: pxr.index(",")]) + 10000000000000
            py = int(pyr) + 10000000000000
            mode += 1
            continue

    t = tokens_linalg((ax, ay), ca, (bx, by), cb, (px, py))
    result += t if t != float("inf") else 0
    return result


test_inp = None
with open("res/day13a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY 13:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day13.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 13:")
print(part1(inp))
print(part2(inp))
