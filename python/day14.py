from util import (
    ints,
)


def part1(inp, size=(101, 103)):
    quadrants = [0, 0, 0, 0]
    for line in inp:
        px, py, vx, vy = ints(line)
        tx = (vx * 100 + px) % size[0]
        ty = (vy * 100 + py) % size[1]
        if tx < size[0] // 2 and ty < size[1] // 2:
            quadrants[0] += 1
        elif tx > size[0] // 2 and ty < size[1] // 2:
            quadrants[1] += 1
        elif tx < size[0] // 2 and ty > size[1] // 2:
            quadrants[2] += 1
        elif tx > size[0] // 2 and ty > size[1] // 2:
            quadrants[3] += 1
    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]


def part2(inp, size=(101, 103), incidences=3):
    robots = []
    seen_incidence = 0
    for line in inp:
        px, py, vx, vy = ints(line)
        robots.append((px, py, vx, vy))
    count = 0
    while True:
        count += 1
        seen = set()
        next = []
        for px, py, vx, vy in robots:
            next.append(((px + vx) % size[0], (py + vy) % size[1], vx, vy))
            seen.add(((px + vx) % size[0], (py + vy) % size[1]))
            if len(seen) == len(robots):
                for i in range(size[1]):
                    for j in range(size[0]):
                        if (j, i) in seen:
                            print("#", end="")
                        else:
                            print(".", end="")
                    print()
                seen_incidence += 1
            if seen_incidence == incidences:
                return count
        robots = next


test_inp = None
with open("res/day14a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 14:")
print(part1(test_inp, (11, 7)))
print()

inp = None
with open("res/day14.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 14:")
print(part1(inp, (101, 103)))
print(part2(inp, (101, 103), 3))
