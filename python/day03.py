import re


def part1(inp):
    result = 0
    for line in inp:
        for match in re.finditer(r"mul\((\d+),(\d+)\)", line):
            result += int(match.group(1)) * int(match.group(2))
    return result


def part2(inp):
    result = 0
    enabled = True
    for line in inp:
        for match in re.finditer(r"(do\(\)|don't\(\)|mul\(\d+,\d+\))", line):
            if match.group(1) == "do()":
                enabled = True
            elif match.group(1) == "don't()":
                enabled = False
            elif enabled:
                split = (
                    match.group(1)
                    .replace("(", "")
                    .replace(")", "")
                    .replace("mul", "")
                    .split(",")
                )
                result += int(split[0]) * int(split[1])
    return result


test_inp = None
with open("res/day03a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY 03:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day03.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 03:")
print(part1(inp))
print(part2(inp))
