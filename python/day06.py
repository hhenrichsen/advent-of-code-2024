from collections import defaultdict
from typing import Tuple
from tqdm import tqdm

from util import Grid

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def part1(inp: Grid):
    tracked = set()
    start = inp.filter(lambda x: x.data == "^")[0]
    direction = 0
    while True:
        prev = start
        start = inp[
            (
                start.x + directions[direction % len(directions)][0],
                start.y + directions[direction % len(directions)][1],
            )
        ]
        if start is None:
            break

        if start.data == "#":
            start = prev
            direction += 1
            continue

        else:
            tracked.add((start.x, start.y))
            continue
    return len(tracked)


def has_loop(grid: Grid, obstacle: Tuple[int, int]) -> bool:
    tracked = defaultdict(set)

    grid = grid.clone()
    start = grid.filter(lambda x: x.data == "^")[0]
    grid[obstacle].data = "#"
    di = 0
    direction = directions[di]

    while True:
        prev = start
        start = start + direction
        if start is None:
            return False

        if start.data == "#":
            start = prev
            tracked[(prev.x, prev.y)].add(di)
            di = (di + 1) % len(directions)
            direction = directions[di]
            continue

        # check if we have been here before
        if di in tracked[start.position()]:
            return True

        tracked[(prev.x, prev.y)].add(di)


def part2(inp: Grid):
    ans = 0

    for o in tqdm(inp.filter(lambda x: x.data == ".")):
        if has_loop(inp, o.position()):
            ans += 1

    return ans


test_inp = Grid.read("res/day06a.txt")
print("TEST DAY 06:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = Grid.read("res/day06.txt")
print("FINAL DAY 06:")
print(part1(inp))
print(part2(inp))
