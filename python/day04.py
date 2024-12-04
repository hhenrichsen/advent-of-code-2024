from collections import Counter

from util import (
    Grid,
)


grid = True
debug = False


def part1(inp: Grid):
    result = 0
    starts = inp.filter(lambda x: x.data == "X")
    if debug:
        visited = set()
    for x in starts:
        ms = x.filter_neighbors(lambda x: x.data == "M", diagonal=True)
        for m in ms:
            direction = (m.x - x.x, m.y - x.y)
            pa = inp[(m.x + direction[0], m.y + direction[1])]
            ps = inp[(m.x + 2 * direction[0], m.y + 2 * direction[1])]
            if pa is not None and pa.data == "A" and ps is not None and ps.data == "S":
                result += 1
                if debug:
                    visited.add((x.x, x.y))
                    visited.add((m.x, m.y))
                    visited.add((pa.x, pa.y))
                    visited.add((ps.x, ps.y))

    if debug:
        print(inp.to_string(lambda x: x.data if (x.x, x.y) in visited else "."))
    return result


def part2(inp):
    result = 0
    starts = inp.filter(lambda x: x.data == "A")
    visited = set()
    for x in starts:
        ms = x.filter_neighbors(
            lambda x: x.data == "M", horizontal=False, vertical=False, diagonal=True
        )
        crosses = 0
        if debug:
            staged = set()
        for m in ms:
            direction = (m.x - x.x, m.y - x.y)
            pa = inp[(x.x - direction[0], x.y - direction[1])]
            if pa is not None and pa.data == "S":
                crosses += 1
                if debug:
                    staged.add((x.x, x.y))
                    staged.add((m.x, m.y))
                    staged.add((pa.x, pa.y))
        if crosses == 2:
            result += 1
            if debug:
                visited.update(staged)

    if debug:
        print(inp.to_string(lambda x: x.data if (x.x, x.y) in visited else "."))
    return result


test_inp = Grid.read("res/day04a.txt")

print("TEST DAY 04:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = Grid.read("res/day04.txt")

print("FINAL DAY 04:")
print(part1(inp))
print(part2(inp))
