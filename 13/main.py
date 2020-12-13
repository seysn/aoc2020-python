from functools import reduce


def part1(timestamp, ids):
    earliest_bus = (0, max(ids))
    for i in ids:
        if i == 0:
            continue
        minutes = i - (timestamp % i)
        if minutes < earliest_bus[1]:
            earliest_bus = (i, minutes)
    return earliest_bus[0] * earliest_bus[1]


assert part1(939, [7, 13, 0, 0, 59, 0, 31, 19]) == 295


def chinese_remainder(n, a):
    """Taken from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python"""
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    """Taken from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python"""
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def part2(ids):
    """Also solvable with https://www.dcode.fr/restes-chinois"""
    a = []
    n = []
    for i, v in enumerate(ids):
        if v != 0:
            a.append(-i)
            n.append(v)
    res = chinese_remainder(n, a)
    return res


assert part2([17, 0, 13, 19]) == 3417
assert part2([7, 13, 0, 0, 59, 0, 31, 19]) == 1068781

if __name__ == "__main__":
    with open("13/input.txt") as f:
        timestamp = int(f.readline())
        ids = [int(i) if i.isnumeric() else 0 for i in f.readline().split(",")]
    print(part1(timestamp, ids))
    print(part2(ids))