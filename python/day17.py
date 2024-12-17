from typing import List


def adv(state, b):
    a = state["a"]
    state["a"] = a // (2 ** combo[b](state))
    state["ip"] += 2
    return state


def bxl(state, b):
    a = state["b"]
    state["b"] = a ^ b
    state["ip"] += 2
    return state


def bst(state, b):
    state["b"] = combo[b](state) % 8
    state["ip"] += 2
    return state


def jnz(state, b):
    if state["a"] != 0:
        state["ip"] = b
        return state
    state["ip"] += 2
    return state


def bxc(state, b):
    xor = state["b"] ^ state["c"]
    state["b"] = xor
    state["ip"] += 2
    return state


def out(state, b):
    state["out"] += f"{combo[b](state) % 8},"
    state["ip"] += 2
    return state


def bdv(state, b):
    a = state["a"]
    state["b"] = a // (2 ** combo[b](state))
    state["ip"] += 2
    return state


def cdv(state, b):
    a = state["a"]
    state["c"] = a // (2 ** combo[b](state))
    state["ip"] += 2
    return state


ops = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

opname = {
    0: "adv",
    1: "bxl",
    2: "bst",
    3: "jnz",
    4: "bxc",
    5: "out",
    6: "bdv",
    7: "cdv",
}


combo = {
    0: lambda state: 0,
    1: lambda state: 1,
    2: lambda state: 2,
    3: lambda state: 3,
    4: lambda state: state["a"],
    5: lambda state: state["b"],
    6: lambda state: state["c"],
}


def part1(inp: List[str]):
    a, b, c, _, program = inp
    a = int(a.split()[-1])
    b = int(b.split()[-1])
    c = int(c.split()[-1])
    instructions = list(map(int, program[9:].split(",")))
    state = {
        "ip": 0,
        "out": "",
        "a": a,
        "b": b,
        "c": c,
    }
    while state["ip"] < len(instructions):
        op = instructions[state["ip"]]
        pair = instructions[state["ip"] + 1]
        state = ops[op](state, pair)
    return state["out"][:-1]


def run(start: int):
    a = start
    o = ""
    while a != 0:
        b = a % 8
        b = b ^ 5
        c = a // (1 << b)
        b = b ^ 6
        a = a // 8
        b = b ^ c
        o += str(b % 8)
    return o


def part2(inp: List[str]):
    _, _, _, _, program = inp
    program = program[9:].replace(",", "")
    chunks = [(len(program) - 1, 0)]
    for space, chunk in chunks:
        for a in range(chunk * 8, chunk * 8 + 8):
            if run(a) == program[space:]:
                chunks += [(space - 1, a)]
                if space == 0:
                    return a


print("TEST DAY 17:")
test_inp = None
with open("res/day17a.txt") as f:
    test_inp = list(map(lambda s: s.strip(), f.readlines()))
print(part1(test_inp))
print(part2(test_inp))
print()

print("FINAL DAY 17:")
inp = None
with open("res/day17.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))
print(part1(inp))
print(part2(inp))
