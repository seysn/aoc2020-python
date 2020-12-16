def parse_input(text):
    text = text.split("\n\n")
    ranges = [l[l.index(":") + 2 :].split(" or ") for l in text[0].split("\n")]
    ranges = [
        tuple(map(int, item.split("-"))) for sublist in ranges for item in sublist
    ]
    ranges = [range(a, b + 1) for a, b in ranges]
    ranges = list(zip(*[iter(ranges)] * 2))
    keys = [l[: l.index(":")] for l in text[0].split("\n")]
    ranges = {k: v for k, v in zip(keys, ranges)}

    tickets = [tuple(map(int, text[1].split("\n")[1].split(",")))]

    for t in text[2].split("\n")[1:]:
        tickets.append(tuple(map(int, t.split(","))))
    return ranges, tickets


def part1(ranges, tickets):
    res = 0
    ranges = [item for sublist in ranges.values() for item in sublist]
    for t in tickets:
        for field in t:
            if not any([field in r for r in ranges]):
                res += field
    return res


def discard_invalids(ranges, tickets):
    valids = []
    ranges = [item for sublist in ranges.values() for item in sublist]
    for t in tickets:
        valid = True
        for field in t:
            if not any([field in r for r in ranges]):
                valid = False
        if valid:
            valids.append(t)
    return valids


def flatten_choices(ticket):
    res = {}
    while ticket:
        tmp = {k: v for k, v in ticket.items() if len(v) == 1}
        for k, v in tmp.items():
            v = v[0]
            res[v] = k
            del ticket[k]
            for kk, vv in ticket.items():
                if v in vv:
                    ticket[kk].remove(v)
    return res


assert flatten_choices(
    {11: ["row"], 12: ["class", "row"], 13: ["class", "row", "seat"]}
) == {"row": 11, "class": 12, "seat": 13}


def search_fields(ranges, tickets):
    ticket = {k: [] for k in tickets[0]}
    tickets = discard_invalids(ranges, tickets)
    fields = list(zip(*tickets[1:]))
    for t, f in zip(tickets[0], fields):
        for k, r in ranges.items():
            if all(
                [a or b for a, b in zip([t in r[0] for t in f], [t in r[1] for t in f])]
            ):
                ticket[t].append(k)
    return flatten_choices(ticket)


def part2(ranges, tickets):
    ticket = search_fields(ranges, tickets)
    departure = {k: v for k, v in ticket.items() if k.startswith("departure")}
    res = 1
    for d in departure.values():
        res *= d
    return res


rexample, texample = parse_input(
    """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
)
assert part1(rexample, texample) == 71
assert discard_invalids(rexample, texample) == [(7, 1, 14), (7, 3, 47)]

rexample, texample = parse_input(
    """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
)
assert search_fields(rexample, texample) == {"row": 11, "class": 12, "seat": 13}

if __name__ == "__main__":
    with open("16/input.txt") as f:
        ranges, tickets = parse_input(f.read())
    print(part1(ranges, tickets))
    print(part2(ranges, tickets))
