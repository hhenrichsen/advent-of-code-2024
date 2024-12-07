def part1(inp: list[str]):
    result = 0
    for line in inp:
        totalStr, parts = line.split(":")
        total = int(totalStr)
        numbers = list(map(int, parts.strip().split(" ")))
        ops = [lambda x, y: x + y, lambda x, y: x * y]
        last = [numbers[0]]
        for i in range(1, len(numbers)):
            curr = numbers[i]
            last = [op(l, curr) for op in ops for l in last]
        if total in last:
            result += total

    return result


def part2(inp):
    result = 0
    for line in inp:
        totalStr, parts = line.split(":")
        total = int(totalStr)
        numbers = list(map(int, parts.strip().split(" ")))
        ops = [
            lambda x, y: x + y,
            lambda x, y: x * y,
            lambda x, y: int(str(x) + str(y)),
        ]
        last = [numbers[0]]
        for i in range(1, len(numbers)):
            curr = numbers[i]
            last = [op(l, curr) for op in ops for l in last]
        if total in last:
            result += total

    return result


test_inp = None
with open("res/day07a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY 07:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day07.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 07:")
print(part1(inp))
print(part2(inp))
