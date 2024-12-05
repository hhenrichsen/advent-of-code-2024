from collections import deque, defaultdict

from util import (
    windows,
)


def part1(inp):
    result = 0
    rules = True
    graph = defaultdict(set)
    for line in inp:
        if line == "":
            rules = False
            continue
        if rules:
            inrule, outrule = map(int, line.split("|"))
            graph[inrule] = set(list(graph[inrule]) + [outrule])
        else:
            pages = list(map(int, line.split(",")))
            if is_ordered(pages, graph):
                result += pages[len(pages) // 2]

    return result


def is_ordered(pages, d):
    for page, next in windows(pages, 2):
        if not page in d:
            break
        if not next in d[page]:
            break
    else:
        return True
    return False


def part2(inp):
    result = 0
    rules = True
    graph = defaultdict(set)

    for line in inp:
        if line == "":
            rules = False
            continue
        if rules:
            inrule, outrule = map(int, line.split("|"))
            graph[inrule] = set(list(graph[inrule]) + [outrule])
        else:
            pages = list(map(int, line.split(",")))
            valid_pages = set(pages)

            if is_ordered(pages, graph):
                continue

            degree = defaultdict(int)
            mini_graph = defaultdict(set)

            for inrule in graph:
                for outrule in graph[inrule]:
                    if outrule in valid_pages and inrule in valid_pages:
                        mini_graph[outrule].add(inrule)
                        degree[inrule] += 1

            q = deque([page for page in pages if degree[page] == 0])
            newpages = []

            while q:
                next = q.popleft()
                newpages.append(next)
                for next_out in mini_graph[next]:
                    degree[next_out] -= 1
                    if degree[next_out] == 0:
                        q.append(next_out)

            result += newpages[len(newpages) // 2]

    return result


test_inp = None
with open("res/day05a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))


print("TEST DAY 05:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day05.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print("FINAL DAY 05:")
print(part1(inp))
print(part2(inp))
