from collections import defaultdict, deque

from util import (
    Grid,
    chunks,
)

grid = False


def part1(inp):
    maze, instructions = chunks(inp)
    print(maze)
    grid = Grid.parse(maze)
    instructions = "".join(instructions)
    robot = grid.filter(lambda c: c.data in "@")[0]
    directions = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1),
    }

    def move(robot: Grid.GridItem[str], direction):
        dx, dy = directions[direction]
        if (
            goal := robot.raycast((dx, dy), lambda c: c.data == "." or c.data == "#")
        ) is not None:
            if goal.data == "#":
                return robot
            curr = goal
            while curr.position() != robot.position():
                x, y = curr.position()
                next = grid[(x - dx, y - dy)]
                grid[(x, y)].data = next.data
                next.data = "."
                curr = next
            return robot + (dx, dy)
        return robot

    for i, c in enumerate(instructions):
        robot = move(robot, c)

    print(grid.to_string(lambda c: c.data))
    return sum(map(lambda c: c.x + c.y * 100, grid.filter(lambda c: c.data == "O")))


def part2(inp):
    maze, instructions = chunks(inp)
    newmaze = []
    for line in maze:
        newline = ""
        for ch in line:
            if ch == "@":
                newline += "@."
            if ch == "O":
                newline += "[]"
            if ch == "#":
                newline += "##"
            if ch == ".":
                newline += ".."
        newmaze.append(newline)
    grid = Grid.parse(newmaze)
    instructions = "".join(instructions)
    robot = grid.filter(lambda c: c.data in "@")[0]
    directions = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1),
    }

    def move(robot: Grid.GridItem[str], direction):
        dx, dy = directions[direction]
        if dy == 0:
            if (
                goal := robot.raycast(
                    (dx, dy), lambda c: c.data == "." or c.data == "#"
                )
            ) is not None:
                if goal.data == "#":
                    return robot
                curr = goal
                while curr.position() != robot.position():
                    x, y = curr.position()
                    next = grid[(x - dx, y - dy)]
                    grid[(x, y)].data = next.data
                    next.data = "."
                    curr = next
                return robot + (dx, dy)
            return robot
        else:
            next = robot + (dx, dy)
            next_data = next.data
            if next_data == ".":
                (robot + (dx, dy)).data = "@"
                robot.data = "."
                return robot + (dx, dy)
            if next_data == "#":
                return robot

            targets = []
            visited = set()
            by_y = defaultdict(list)
            by_y[robot.y].append(robot)
            search = deque([next])
            while len(search) > 0:
                next = search.popleft()
                if next in visited:
                    continue
                visited.add(next)
                if next.data == "[":
                    search += [
                        next,
                        next.east(),
                        next + (0, dy),
                        (next + (0, dy)).east(),
                    ]
                    by_y[next.y].append(next)
                elif next.data == "]":
                    search += [
                        next,
                        next.west(),
                        next + (0, dy),
                        (next + (0, dy)).west(),
                    ]
                    by_y[next.y].append(next)
                else:
                    targets.append(next)
            if all(map(lambda c: c.data == ".", targets)):
                ordered = sorted(by_y.keys(), reverse=dy != -1)
                for k in ordered:
                    for c in by_y[k]:
                        if c.data == ".":
                            continue
                        (c + (0, dy)).data = c.data
                        c.data = "."
                return robot + (dx, dy)
            else:
                return robot

    for n in instructions:
        robot = move(robot, n)
        print(grid.to_string(lambda c: c.data if c.data != "@" else n))
        print()
    return sum(map(lambda c: c.x + c.y * 100, grid.filter(lambda c: c.data == "[")))


test_inp = None
with open("res/day15a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 15:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day15.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 15:")
print(part1(inp))
print(part2(inp))
