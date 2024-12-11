from functools import cache


def part1(inp):
    line = map(int, (inp[0].split(" ")))
    for _ in range(25):
        nextLine = []
        for el in line:
            if el == 0:
                nextLine.append(1)
            elif len(str(el)) % 2 == 0:
                st = str(el)
                h1 = int(st[: len(st) // 2], 10)
                h2 = int(st[len(st) // 2 :], 10)
                nextLine.append(h1)
                nextLine.append(h2)
            else:
                nextLine.append(el * 2024)
        line = nextLine
    return len(line)


@cache
def stones(n, iters):
    if iters == 0:
        return 1

    if n == 0:
        return stones(1, iters - 1)

    if len(str(n)) % 2 == 0:
        st = str(n)
        h1 = int(st[: len(st) // 2], 10)
        h2 = int(st[len(st) // 2 :], 10)
        return stones(h1, iters - 1) + stones(h2, iters - 1)

    return stones(n * 2024, iters - 1)


def part2(inp):
    parts = list(map(int, (inp[0].split(" "))))
    res = 0
    for part in parts:
        res += stones(part, 75)
    return res


test_inp = None
with open("res/day11a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY 11:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day11.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 11:")
print(part1(inp))
print(part2(inp))
