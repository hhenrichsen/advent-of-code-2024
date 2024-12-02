from util import (
    windows,
)

def part1(inp):
    result = 0
    for line in inp:
        valid = True
        n = list(map(int, line.split(" ")))
        d = (n[0] - n[1])
        if d == 0:
            continue
        s = 1 if d > 0 else -1
        for i, j in windows(n, 2):
            ijs = 1 if i - j > 0 else -1
            if ijs != s:
                valid = False
                break
            ijd = abs(i - j)
            if ijd < 1 or ijd > 3:
                valid = False
                break
        if valid:
            result += 1

    return result


def part2(inp):
    result = 0
    for line in inp:
        n = list(map(int, line.split(" ")))
        options = []
        for i in range(len(n)):
            options.append(n[0:i] + n[i+1:])
        valid = False
        for n in options:
            d = (n[0] - n[1])
            if d == 0:
                continue
            s = 1 if d > 0 else -1
            for i, j in windows(n, 2):
                ijs = 1 if i - j > 0 else -1
                if ijs != s:
                    break

                ijd = abs(i - j)
                if ijd < 1 or ijd > 3:
                    break
            else:
                valid = True
                print(f"Option {n} is valid")

            if valid:
                result += 1
                break

    return result


test_inp = None
with open("res/day02a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 02:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day02.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 02:")
print(part1(inp))
print(part2(inp))
    