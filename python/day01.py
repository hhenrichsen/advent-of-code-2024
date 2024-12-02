from collections import Counter

            
def part1(inp):
    sum = 0
    left = []
    right = []
    for line in inp:
        a, b = line.split("   ")
        left.append(a)
        right.append(b)
    sorted_right = sorted(right)
    sorted_left = sorted(left)
    differences = []
    for a, b in zip(sorted_left, sorted_right):
        differences.append(abs(int(b) - int(a)))
    for diff in differences:
        sum += diff
    return sum


def part2(inp):
    sum = 0
    left = []
    right = []
    for line in inp:
        a, b = line.split("   ")
        left.append(int(a))
        right.append(int(b))
    sorted_left = sorted(left)
    counted_right = Counter(right)
    differences = []
    for a in sorted_left:
        differences.append(a * counted_right[a])
    for diff in differences:
        sum += diff
    return sum

test_inp = None
with open("res/day01a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 01:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day01.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 01:")
print(part1(inp))
print(part2(inp))
    