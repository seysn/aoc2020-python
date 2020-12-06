from collections import Counter

def part1(declarations):
    res = 0
    for d in declarations:
        tmp = set()
        for person in d:
            tmp |= set(person)
        res += len(tmp)
    return res

def part2(declarations):
    res = 0
    for d in declarations:
        tmp = Counter()
        for person in d:
            tmp += Counter(person)
        for _, v in tmp.items():
            if v == len(d):
                res += 1
    return res

if __name__ == "__main__":
    declarations = []
    with open("06/input.txt") as f:
        declarations = [groups.split('\n') for groups in f.read().split("\n\n")]
    print(part1(declarations))
    print(part2(declarations))