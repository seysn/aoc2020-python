import itertools


def generate_valids(preamble):
    return [a + b for (a, b) in itertools.combinations(preamble, 2)]


def part1(numbers, preamble=25):
    for i in range(preamble, len(numbers)):
        valids = generate_valids(numbers[i - preamble : i])
        if numbers[i] not in valids:
            return numbers[i]
    return 0


def part2(numbers, invalid_num):
    for i in range(3, len(numbers)):
        for j in range(0, len(numbers) - i):
            nums = numbers[j : j + i]
            if sum(nums) == invalid_num:
                return max(nums) + min(nums)
    return 0


example = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
parsed_example = [int(l) for l in example.split("\n")]
assert part1(parsed_example, 5) == 127
assert part2(parsed_example, 127) == 62

if __name__ == "__main__":
    numbers = []
    with open("09/input.txt") as f:
        numbers = [int(l.strip()) for l in f.readlines()]
    invalid_num = part1(numbers)
    print(invalid_num)
    print(part2(numbers, invalid_num))
