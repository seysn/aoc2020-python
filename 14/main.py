import re
from itertools import product


def apply_mask(value, mask):
    bin_value = bin(value)[2:].rjust(len(mask), "0")
    return int("".join([bv if bm == "X" else bm for bv, bm in zip(bin_value, mask)]), 2)


def address_combination(value, mask):
    bin_value = bin(value)[2:].rjust(len(mask), "0")
    masked = "".join([bv if bm == "0" else bm for bv, bm in zip(bin_value, mask)])
    nx = masked.count("X")
    masked = masked.replace("X", "{}")
    res = []
    for p in product("01", repeat=nx):
        res.append(int(masked.format(*p), 2))
    return res


# fmt: off
assert apply_mask(11, "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X") == 73
assert address_combination(42, "000000000000000000000000000000X1001X") == [26, 27, 58, 59]
# fmt: on


def part1(program):
    mem = {}
    mask = None
    for inst in program:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            mem[inst[0]] = apply_mask(inst[1], mask)
    return sum(mem.values())


def part2(program):
    mem = {}
    mask = None
    for inst in program:
        if inst[0] == "mask":
            mask = inst[1]
        else:
            for addr in address_combination(inst[0], mask):
                mem[addr] = inst[1]
    return sum(mem.values())


# fmt: off
example = [("mask", "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"), (8, 11), (7, 101), (8, 0)]
example2 = [("mask", "000000000000000000000000000000X1001X"), (42, 100), ("mask", "00000000000000000000000000000000X0XX"), (26, 1)]
assert part1(example) == 165
assert part2(example2) == 208
# fmt: on

if __name__ == "__main__":
    program = []
    with open("14/input.txt") as f:
        for l in f:
            if l[:4] == "mask":
                program.append(("mask", l[7:].strip()))
            else:
                program.append(
                    tuple(map(int, re.findall("mem\[(\d+)\] = (\d+)", l.strip())[0]))
                )
    print(part1(program))
    print(part2(program))
