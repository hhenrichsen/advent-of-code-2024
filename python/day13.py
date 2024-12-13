from typing import Tuple

from util import chunks, ints


def tokens(
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
    ca, cb = 3, 1
    for chunk in chunks(inp):
        a, b, p = chunk
        ax, ay = ints(a)
        bx, by = ints(b)
        px, py = ints(p)
        t = tokens((ax, ay), ca, (bx, by), cb, (px, py))
        result += t if t != float("inf") else 0
    return result


def part2(inp):
    result = 0
    ca, cb = 3, 1
    for chunk in chunks(inp):
        a, b, p = chunk
        ax, ay = ints(a)
        bx, by = ints(b)
        px, py = list(map(lambda a: a + 10000000000000, ints(p)))
        t = tokens((ax, ay), ca, (bx, by), cb, (px, py))
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
