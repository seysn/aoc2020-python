import itertools


def part1(entries):
    for entry in entries:
        if (2020 - entry) in entries:
            return entry * (2020 - entry)
    return 0


def part2(entries):
    for p in itertools.permutations(entries, 3):
        if sum(p) == 2020:
            return p[0] * p[1] * p[2]
    return 0


assert part1([1721, 979, 366, 299, 675, 1456]) == 514579
assert part2([1721, 979, 366, 299, 675, 1456]) == 241861950


if __name__ == "__main__":
    entries = []
    with open("01/input.txt") as f:
        entries = list(map(int, f.readlines()))
    print(part1(entries))
    print(part2(entries))
