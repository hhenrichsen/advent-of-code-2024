from tqdm import tqdm


def part1(inp):
    result = 0
    inp = inp[0]
    nums = list(map(int, list(inp)))
    places = []
    id = 0
    for i in range(0, len(nums), 2):
        l = nums[i]
        s = nums[i + 1] if i + 1 < len(nums) else 0

        for i in range(l):
            places.append(id)
        for i in range(s):
            places.append(None)
        id += 1

    mindex = 0
    for i in range(len(places) - 1, -1, -1):
        try:
            findex = places.index(None, mindex)
        except ValueError:
            break
        mindex = findex + 1
        places[findex] = places[i]
        places[i] = None

    for i, j in enumerate(places[1:]):
        if j is not None:
            result += i * j
    return result


def part2(inp):
    result = 0
    inp = inp[0]
    nums = list(map(int, list(inp)))
    places = []
    id = 0
    spaces = []
    for blockEnd in range(0, len(nums), 2):
        l = nums[blockEnd]
        s = nums[blockEnd + 1] if blockEnd + 1 < len(nums) else 0

        for blockEnd in range(l):
            places.append(id)
        for blockEnd in range(s):
            places.append(None)
            spaces.append(len(places) - 1)
        id += 1

    moved = set()
    search = None
    for blockEnd in tqdm(range(len(places) - 1, -1, -1)):
        if places[blockEnd] is None or places[blockEnd] in moved:
            continue
        search = places[blockEnd]
        sindex = places.index(search)
        size = 1 + blockEnd - sindex
        moved.add(search)
        for startidx, start in enumerate(spaces):
            if start > blockEnd:
                break
            available = 0
            for i in range(start, len(places)):
                if places[i] is not None:
                    break
                available += 1
            if available >= size:
                for i in range(size):
                    places[start + i] = places[blockEnd - i]
                    places[blockEnd - i] = None
                if size != available:
                    spaces[startidx] = start + size
                else:
                    spaces.pop(startidx)
                break

    for i, j in enumerate(places):
        if j is not None:
            result += i * j
    return result


test_inp = None
with open("res/day09a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))

print("TEST DAY 09:")
print(part1(test_inp))
print(part2(test_inp))
print()

inp = None
with open("res/day09.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))

print("FINAL DAY 09:")
print(part1(inp))
print(part2(inp))
