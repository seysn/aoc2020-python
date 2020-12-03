def part1(trees):
    x = 0
    res = 0
    for line in trees:
        if line[x % len(line)] == "#":
            res += 1
        x += 3
    return res


def part2(trees):
    weight = len(trees[0])
    x, y = 0, 0
    res = 1
    rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for r in rules:
        tmp = 0
        x, y = 0, 0
        while y < len(trees):
            if trees[y][x % weight] == "#":
                tmp += 1
            x += r[0]
            y += r[1]
        res *= tmp
    return res


example = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".split()

assert part1(example) == 7
assert part2(example) == 336

if __name__ == "__main__":
    trees = []
    with open("03/input.txt") as f:
        trees = f.read().split()
    print(part1(trees))
    print(part2(trees))
