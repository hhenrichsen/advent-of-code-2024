from util import (
    Grid,
    windows,
)


def part1(inp: Grid):
    result = 0
    seen = set()
    width, height = inp.size()
    for x in range(width):
        for y in range(height):
            cell = inp[(x, y)]
            if cell in seen:
                continue
            letter = cell.data
            count, items = inp.flood(
                cell.position(),
                lambda c: c.data == letter,
            )
            if len(items) < 1:
                continue
            seen.update(items)

            perimeter = 0
            for item in items:
                perimeter += item.count_neighbor_data(
                    lambda d: d != letter, bounds=False
                )

            result += perimeter * count
    return result


def part2(inp: Grid):
    result = 0
    seen = set()
    width, height = inp.size()
    for x in range(width):
        for y in range(height):
            cell = inp[(x, y)]
            if cell in seen:
                continue
            letter = cell.data
            count, items = inp.flood(
                cell.position(),
                lambda c: c.data == letter,
            )
            if len(items) < 1:
                continue
            seen.update(items)

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (0, 1)]

            outside_corners = list()
            for da, db in windows(directions, 2):
                for item in items:
                    if (not item + da or (item + da).data != letter) and (
                        not item + db or (item + db).data != letter
                    ):
                        outside_corners.append(item)

            inside_corners = []
            for da, db in windows(directions, 2):
                for item in items:
                    if (
                        item + da
                        and (item + da).data == letter
                        and item + db
                        and (item + db).data == letter
                        and (not item + da + db or (item + da + db).data != letter)
                    ):
                        inside_corners.append(item)

            sides = len(outside_corners) + len(inside_corners)
            result += sides * count
    return result


test_inp = Grid.read("res/day12a.txt")

print("TEST DAY 12:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = Grid.read("res/day12.txt")

print("FINAL DAY 12:")
print(part1(inp))
print(part2(inp))
