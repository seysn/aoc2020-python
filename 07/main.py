def clean_rule(rule):
    rule = rule.replace(",", "")
    rule = rule.replace("bags", "")
    rule = rule.replace("bag", "")
    rule = rule.replace("contain", "")
    return rule[:-2]  # dot and newline


def update_dict(res, key, content_key, content_value):
    if key not in res:
        res[key] = {content_key: content_value}
        return res
    if content_key not in res[key]:
        res[key].update({content_key: content_value})
    else:
        res[key][content_key] += content_value
    return res


def parse_input(rules):
    res = {}
    for r in rules:
        if "no" in rules:
            continue
        r = clean_rule(r)
        t = r.split()
        key = t[0] + " " + t[1]
        for i in range(2, len(t[2:]), 3):
            res = update_dict(res, key, t[i + 1] + " " + t[i + 2], int(t[i]))
    return res


def contains_bag(content, options):
    return any([b in options for b in content.keys()])


def count_bag(rules, bag="shiny gold"):
    if bag not in rules:
        return 0
    return sum([v + v * count_bag(rules, k) for k, v in rules[bag].items()])


def part1(rules):
    options = ["shiny gold"]
    prev_len = 1
    while True:
        for k, v in rules.items():
            if contains_bag(v, options) and k not in options:
                options.append(k)
        if len(options) != prev_len:
            prev_len = len(options)
        else:
            break
    return len(options) - 1


def part2(rules):
    return count_bag(rules)


example = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
parsed_example = parse_input(example.split("\n"))
assert part1(parsed_example) == 4
assert part2(parsed_example) == 32

if __name__ == "__main__":
    rules = []
    with open("07/input.txt") as f:
        rules = parse_input(f.readlines())
    print(part1(rules))
    print(part2(rules))
