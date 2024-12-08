from itertools import permutations

from util import Grid


def part1(inp: Grid):
    locations = set()
    letters = inp.filter(lambda c: c.data != ".")
    available_letters = set(map(lambda c: c.data, letters))
    for letter in available_letters:
        letter_nodes = inp.filter(lambda c: c.data == letter)
        pairs = permutations(letter_nodes, 2)
        for a, b in pairs:
            distance = ((a.x - b.x), (a.y - b.y))
            if inp[(a.x + distance[0], a.y + distance[1])] is not None:
                locations.add((a.x + distance[0], a.y + distance[1]))
            if inp[(b.x - distance[0], b.y - distance[1])] is not None:
                locations.add((b.x - distance[0], b.y - distance[1]))

    print(inp.to_string(lambda x: "#" if x.position() in locations else x.data))
    return len(locations)


def part2(inp: Grid):
    locations = set()
    letters = inp.filter(lambda c: c.data != ".")
    available_letters = set(map(lambda c: c.data, letters))
    for letter in available_letters:
        letter_nodes = inp.filter(lambda c: c.data == letter)
        pairs = permutations(letter_nodes, 2)
        for a, b in pairs:
            distance = ((a.x - b.x), (a.y - b.y))
            locations.add((a.x, a.y))
            locations.add((b.x, b.y))
            while inp[(a.x + distance[0], a.y + distance[1])] is not None:
                locations.add((a.x + distance[0], a.y + distance[1]))
                a = inp[(a.x + distance[0], a.y + distance[1])]
            while inp[(b.x - distance[0], b.y - distance[1])] is not None:
                locations.add((b.x - distance[0], b.y - distance[1]))
                b = inp[(b.x - distance[0], b.y - distance[1])]

    print(inp.to_string(lambda x: "#" if x.position() in locations else x.data))
    return len(locations)


test_inp = Grid.read("res/day08a.txt")

print("TEST DAY 08:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = Grid.read("res/day08.txt")

print("FINAL DAY 08:")
print(part1(inp))
print(part2(inp))
