ACTIONS = {
    "N": lambda x, y, d, v: (x, y + v, d),
    "S": lambda x, y, d, v: (x, y - v, d),
    "E": lambda x, y, d, v: (x + v, y, d),
    "W": lambda x, y, d, v: (x - v, y, d),
    "L": lambda x, y, d, v: (x, y, turn_direction(d, v, "L")),
    "R": lambda x, y, d, v: (x, y, turn_direction(d, v, "R")),
    "F": lambda x, y, d, v: ACTIONS[d](x, y, d, v),
}

ACTIONS_WAYPOINT = {
    "N": lambda x, y, wx, wy, v: (x, y, wx, wy + v),
    "S": lambda x, y, wx, wy, v: (x, y, wx, wy - v),
    "E": lambda x, y, wx, wy, v: (x, y, wx + v, wy),
    "W": lambda x, y, wx, wy, v: (x, y, wx - v, wy),
    "L": lambda x, y, wx, wy, v: (x, y, *rotate_waypoint(x, y, wx, wy, v, "L")),
    "R": lambda x, y, wx, wy, v: (x, y, *rotate_waypoint(x, y, wx, wy, v, "R")),
    "F": lambda x, y, wx, wy, v: (
        x + (wx - x) * v,
        y + (wy - y) * v,
        wx + (wx - x) * v,
        wy + (wy - y) * v,
    ),
}


def turn_direction(direction, angle, side):
    dirs = ["N", "E", "S", "W"]
    if side == "R":
        return dirs[(dirs.index(direction) + angle // 90) % 4]
    return dirs[dirs.index(direction) - angle // 90]


def rotate_waypoint(x, y, wx, wy, angle, side):
    dx, dy = wx - x, wy - y
    deltas = [(dx, dy), (dy, -dx), (-dx, -dy), (-dy, dx)]
    if side == "R":
        delta = deltas[angle // 90]
    else:
        delta = deltas[-(angle // 90)]
    return x + delta[0], y + delta[1]


assert turn_direction("E", 90, "R") == "S"
assert turn_direction("E", 90, "L") == "N"
assert turn_direction("S", 270, "R") == "E"
assert turn_direction("S", 270, "L") == "W"

assert rotate_waypoint(0, 0, 1, 2, 90, "R") == (2, -1)
assert rotate_waypoint(0, 0, 1, 2, 90, "L") == (-2, 1)
assert rotate_waypoint(0, 0, 1, 2, 270, "R") == (-2, 1)
assert rotate_waypoint(0, 0, 1, 2, 270, "L") == (2, -1)


def part1(instructions):
    direction = "E"
    x, y = 0, 0
    for a, v in instructions:
        x, y, direction = ACTIONS[a](x, y, direction, v)
    return abs(x) + abs(y)


def part2(instructions):
    x, y, wx, wy = 0, 0, 10, 1
    for a, v in instructions:
        x, y, wx, wy = ACTIONS_WAYPOINT[a](x, y, wx, wy, v)
    return abs(x) + abs(y)


example = [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]
assert part1(example) == 25
assert part2(example) == 286

if __name__ == "__main__":
    instructions = []
    with open("12/input.txt") as f:
        instructions = [(l[0], int(l[1:])) for l in f.readlines()]
    print(part1(instructions))
    print(part2(instructions))
