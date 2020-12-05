def parse_pass(board_pass: str):
    row_min, row_max = 0, 127
    for char in board_pass[:7]:
        diff = row_max - row_min
        if diff % 2 != 0:
            diff += 1
        if char == "F":
            row_max -= diff // 2
        else:
            row_min += diff // 2
    col_min, col_max = 0, 7
    for char in board_pass[7:]:
        diff = col_max - col_min
        if diff % 2 != 0:
            diff += 1
        if char == "L":
            col_max -= diff // 2
        else:
            col_min += diff // 2
    assert row_min == row_max
    assert col_min == col_max
    res = {
        "seat_id": row_min * 8 + col_min,
        "row": row_min,
        "column": col_min
    }
    return res

assert parse_pass("FBFBBFFRLR") == {"seat_id": 357, "row": 44, "column": 5}
assert parse_pass("BFFFBBFRRR") == {"seat_id": 567, "row": 70, "column": 7}
assert parse_pass("FFFBBBFRRR") == {"seat_id": 119, "row": 14, "column": 7}
assert parse_pass("BBFFBBFRLL") == {"seat_id": 820, "row": 102, "column": 4}

def part1(passes) -> int:
    return max([d["seat_id"] for d in map(parse_pass, passes)])

def part2(passes) -> int:
    ids = [d["seat_id"] for d in map(parse_pass, passes)]
    return list(set(range(min(ids), max(ids))) - set(ids))[0]

if __name__ == "__main__":
    passes = []
    with open("05/input.txt") as f:
        passes = f.readlines()
    print(part1(passes))
    print(part2(passes))