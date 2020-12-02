def parse_input(line):
    t = line.split()
    st, end = map(int, t[0].split("-"))
    return st, end, t[1][0], t[2]


def part1(passwords):
    res = 0
    for p in passwords:
        st, end, char, pw = parse_input(p)
        count = pw.count(char)
        if st <= count <= end:
            res += 1
    return res


def part2(passwords):
    res = 0
    for p in passwords:
        st, end, char, pw = parse_input(p)
        if (pw[st - 1] == char) ^ (pw[end - 1] == char):
            res += 1
    return res


if __name__ == "__main__":
    passwords = []
    with open("02/input.txt") as f:
        passwords = f.readlines()
    print(part1(passwords))
    print(part2(passwords))
