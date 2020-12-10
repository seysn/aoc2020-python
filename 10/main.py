def part1(adapters):
    adapters = sorted(adapters)
    adapters = [0] + adapters + [max(adapters) + 3]
    cpt = {1: 0, 2: 0, 3: 0}
    for v in adapters[:-1]:
        for i in cpt.keys():
            if v + i in adapters:
                cpt[i] += 1
                break
    res = 1
    for _, v in cpt.items():
        if v != 0:
            res *= v
    return res


class Adapters:
    def __init__(self, adapters) -> None:
        self.adapters = sorted(adapters)
        self.end = self.adapters[-1]
        self.cache = {}

    def nb_choices(self, adapter):
        if adapter == self.end:
            return 1
        res = 0
        for i in range(1, 4):
            curr = adapter + i
            if curr in self.adapters:
                if curr in self.cache:
                    res += self.cache[curr]
                else:
                    tmp = self.nb_choices(curr)
                    self.cache[curr] = tmp
                    res += tmp
        return res


def part2(adapters):
    res = Adapters([0] + adapters + [max(adapters) + 3]).nb_choices(0)
    return res


# fmt: off
example1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
example2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
assert part1(example1) == 35
assert part1(example2) == 220
assert part2(example1) == 8
assert part2(example2) == 19208
# fmt: on

if __name__ == "__main__":
    adapters = []
    with open("10/input.txt") as f:
        adapters = [int(a) for a in f.readlines()]
    print(part1(adapters))
    print(part2(adapters))