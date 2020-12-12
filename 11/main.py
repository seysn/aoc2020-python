from copy import deepcopy


class Seats:
    def __init__(self, seats) -> None:
        self.seats = seats
        self.height = len(seats)
        self.width = len(seats[0])

    def count(self, x, y):
        count = {"L": 0, ".": 0, "#": 0}
        for i in range(0 if y == 0 else -1, 1 if y == self.height - 1 else 2):
            for j in range(0 if x == 0 else -1, 1 if x == self.width - 1 else 2):
                if i == 0 and j == 0:
                    continue
                count[self.seats[y + i][x + j]] += 1
        return count

    def next_all_seats(self):
        next_seats = deepcopy(self.seats)
        for y in range(self.height):
            for x in range(self.width):
                self.next_seat(next_seats, x, y)
        if self.seats == next_seats:
            return False
        self.seats = next_seats
        return True

    def next_seat(self, seats, x, y):
        count = self.count(x, y)
        if self.seats[y][x] == "L":
            if count["#"] == 0:
                seats[y][x] = "#"
        elif self.seats[y][x] == "#":
            if count["#"] >= 4:
                seats[y][x] = "L"

    # fmt: off
    def count2(self, x, y):
        count = {"L": 0, "#": 0}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for d in directions:
            pos = (x + d[0], y + d[1])
            while pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height:
                seat = self.seats[pos[1]][pos[0]]
                if seat != ".":
                    count[seat] += 1
                    break
                pos = (pos[0] + d[0], pos[1] + d[1])
        return count
    # fmt: on

    def next_all_seats2(self):
        next_seats = deepcopy(self.seats)
        for y in range(self.height):
            for x in range(self.width):
                self.next_seat2(next_seats, x, y)
        if self.seats == next_seats:
            return False
        self.seats = next_seats
        return True

    def next_seat2(self, seats, x, y):
        count = self.count2(x, y)
        if self.seats[y][x] == "L":
            if count["#"] == 0:
                seats[y][x] = "#"
        elif self.seats[y][x] == "#":
            if count["#"] >= 5:
                seats[y][x] = "L"

    def occupied_seats(self):
        return sum([l.count("#") for l in self.seats])


def part1(seats):
    seats = Seats(seats)
    while seats.next_all_seats():
        pass
    res = seats.occupied_seats()
    return res


def part2(seats):
    seats = Seats(seats)
    while seats.next_all_seats2():
        pass
    res = seats.occupied_seats()
    return res


example = [
    ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
    ["L", "L", "L", "L", "L", "L", "L", ".", "L", "L"],
    ["L", ".", "L", ".", "L", ".", ".", "L", ".", "."],
    ["L", "L", "L", "L", ".", "L", "L", ".", "L", "L"],
    ["L", ".", "L", "L", ".", "L", "L", ".", "L", "L"],
    ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
    [".", ".", "L", ".", "L", ".", ".", ".", ".", "."],
    ["L", "L", "L", "L", "L", "L", "L", "L", "L", "L"],
    ["L", ".", "L", "L", "L", "L", "L", "L", ".", "L"],
    ["L", ".", "L", "L", "L", "L", "L", ".", "L", "L"],
]

example2 = [
    [".", ".", ".", ".", ".", ".", ".", "#", "."],
    [".", ".", ".", "#", ".", ".", ".", ".", "."],
    [".", "#", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", "L", ".", ".", ".", ".", "#"],
    [".", ".", ".", ".", "#", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "#", ".", ".", ".", ".", "."],
]

example3 = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "L", ".", "L", ".", "#", ".", "#", ".", "#", ".", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

assert part1(example) == 37
assert Seats(example2).count2(3, 4) == {"L": 0, "#": 8}
assert Seats(example3).count2(1, 1) == {"L": 1, "#": 0}
assert part2(example) == 26

if __name__ == "__main__":
    seats = []
    with open("11/input.txt") as f:
        seats = [list(l.strip()) for l in f.readlines()]
    print(part1(seats))
    print(part2(seats))