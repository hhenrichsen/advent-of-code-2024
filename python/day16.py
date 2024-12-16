import heapq
from util import Grid

is_grid = True


def part1g(inp: Grid):
    result = 0
    start = inp.filter(lambda c: c.data == "S")[0]
    end = inp.filter(lambda c: c.data == "E")[0]
    q = []
    visited = set()
    heapq.heappush(q, (0, (start, [], (1, 0))))
    while len(q) > 0:
        cost, m = heapq.heappop(q)
        cell, history, last = m
        if cell == end:
            print(inp.to_string(lambda c: "O" if c in set(history) else c.data))
            return cost
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_cell = cell + (dx, dy)
            if next_cell in visited:
                continue
            if next_cell.data == "#":
                continue
            visited.add(next_cell)
            heapq.heappush(
                q,
                (
                    cost + 1001 if last != (dx, dy) else cost + 1,
                    (next_cell, history + [next_cell], (dx, dy)),
                ),
            )
    return result


def part2g(inp: Grid):
    start = inp.filter(lambda c: c.data == "S")[0]
    end = inp.filter(lambda c: c.data == "E")[0]
    q = []
    paths = set()
    heapq.heappush(q, (0, (start, [], (1, 0))))
    min_cost = None
    seen = dict()
    while len(q) > 0:
        cost, m = heapq.heappop(q)
        cell, history, last = m
        if min_cost and cost > min_cost:
            break

        if (cell.position(), last) in seen and seen[(cell.position(), last)] < cost:
            continue
        seen[(cell.position(), last)] = cost

        if cell == end and (min_cost is None or cost == min_cost):
            min_cost = cost
            paths.update(history)
            continue

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_cell = cell + (dx, dy)
            next_cost = cost + 1001 if last != (dx, dy) else cost + 1
            if next_cell.data == "#":
                continue
            if next_cell.position() in set(history):
                continue
            heapq.heappush(
                q,
                (
                    next_cost,
                    (next_cell, history + [next_cell.position()], (dx, dy)),
                ),
            )
    print(inp.to_string(lambda c: "O" if c.position() in paths else c.data))
    return len(paths) + 1


print("TEST DAY 16:")
test_inp = Grid.read("res/day16a.txt")
print(part1g(test_inp))
print(part2g(test_inp))
print()

print("FINAL DAY 16:")
inp = Grid.read("res/day16.txt")
print(part1g(inp))
print(part2g(inp))
