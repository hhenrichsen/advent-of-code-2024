import sys

_, day = sys.argv

if open(f"./res/day{day}.txt", "r").read() != "" \
    or open(f"./res/day{day}a.txt", "r").read() != "" \
    or open(f"./python/day{day}.py", "r").read() != "":
    print(f"Day {day} already exists")
    exit(1)

with open(f"./res/day{day}.txt", "w") as f:
    f.write("")

with open(f"./res/day{day}a.txt", "w") as f:
    f.write("")

with open(f"./python/day{day}.py", "w") as f:
    f.write(
        f"""
from util import (
    AfterRegion,
    Grid,
    InputParser,
    Interval,
    RangeRegion,
    RestRegion,
    UntilRegion,
    breadth_first_search,
    compare_x,
    compare_y,
    compose_fns,
    discard,
    either,
    eq,
    intersect_strings,
    inv,
    is_in,
    ne,
    not_in,
    re_whitespace_segmenter,
    segmented_lines,
    sort_lambda,
    space_segmenter,
    stripped_lines,
    whitespace_numbers,
    windows,
)

grid = False

            
def part1(inp):
    sum = 0
    for line in inp:
        ...
    return sum


def part2(inp):
    sum = 0
    for line in inp:
        ...
    return sum

if not grid:
    test_inp = None
    with open("res/day{day}a.txt") as f:
        test_inp = list(map(lambda s: s.strip(), f.readlines()))
else:
    test_inp = Grid.read("res/day{day}a.txt")


print("TEST DAY {day}:")
print(part1(test_inp))
print(part2(test_inp))
print()

if not grid:
    inp = None
    with open("res/day{day}.txt") as f:
        inp = list(map(lambda s: s.strip(), f.readlines()))
else:
    inp = Grid.read("res/day{day}.txt")


print("FINAL DAY {day}:")
print(part1(inp))
print(part2(inp))
    """
    )
