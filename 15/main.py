def solve(numbers, nloop):
    res = {}
    for i, v in enumerate(numbers):
        res[v] = (-1, i)
    last = numbers[-1]
    for i in range(len(numbers), nloop):
        if res[last][0] == -1:
            last = 0
        else:
            last = res[last][1] - res[last][0]
        if last in res:
            res[last] = (res[last][1], i)
        else:
            res[last] = (-1, i)
    return last


def part1(numbers):
    return solve(numbers, 2020)


assert part1([0, 3, 6]) == 436
assert part1([1, 3, 2]) == 1
assert part1([2, 1, 3]) == 10


def part2(numbers):
    return solve(numbers, 30000000)


if __name__ == "__main__":
    numbers = [14, 8, 16, 0, 1, 17]
    print(part1(numbers))
    print(part2(numbers))
