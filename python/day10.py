from collections import defaultdict

from util import Grid

grid = True


def score_node(node: Grid.GridItem, backtr: dict):
    layer = backtr[node.position()]
    tops = set()
    while len(layer) > 0:
        next = []
        for n in layer:
            if n.data == "9":
                tops.add(n)
                continue
            for nx in backtr[n.position()]:
                next.append(nx)
        layer = next
    return len(tops)


def score_node2(node: Grid.GridItem, backtr: dict):
    score = 0
    layer = backtr[node.position()]
    while len(layer) > 0:
        next = []
        for n in layer:
            if n.data == "9":
                score += 1
            for nx in backtr[n.position()]:
                next.append(nx)
        layer = next
    return score


def part1(inp: Grid):
    nines = inp.filter(lambda x: x.data == "9")
    curr = set(nines)
    backtr = defaultdict(list)
    for i in range(9, -1, -1):
        next = set()
        for c in curr:
            neighbors = c.filter_neighbor_data(lambda x: int(x) == i - 1)
            for n in neighbors:
                backtr[n.position()].append(c)
                next.add(n)
        if len(next) == 0:
            break
        curr = next
    return sum(map(lambda x: score_node(x, backtr), curr))


def part2(inp):
    nines = inp.filter(lambda x: x.data == "9")
    curr = set(nines)
    backtr = defaultdict(list)
    for i in range(9, -1, -1):
        next = set()
        for c in curr:
            neighbors = c.filter_neighbor_data(lambda x: int(x) == i - 1)
            for n in neighbors:
                backtr[n.position()].append(c)
                next.add(n)
        if len(next) == 0:
            break
        curr = next
    return sum(map(lambda x: score_node2(x, backtr), curr))


test_inp = Grid.read("res/day10a.txt")

print("TEST DAY 10:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = Grid.read("res/day10.txt")

print("FINAL DAY 10:")
print(part1(inp))
print(part2(inp))
