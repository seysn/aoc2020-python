import re
import string

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def parse_input(text: str):
    passports = []
    for p in text.split("\n\n"):
        tmp = {}
        for d in re.findall(r"[\w:#]+", p):
            k, v = d.split(":")
            tmp[k] = v
        passports.append(tmp)
    return passports


def keys_present(passport: dict):
    for k in mandatory_keys:
        if k not in passport.keys():
            return False
    return True


def is_valid(passport: dict):
    if not keys_present(passport):
        return False
    for k, v in passport.items():
        if k == "byr":
            if not v.isnumeric():
                return False
            if not (1920 <= int(v) <= 2002):
                return False
        elif k == "iyr":
            if not v.isnumeric():
                return False
            if not (2010 <= int(v) <= 2020):
                return False
        elif k == "eyr":
            if not v.isnumeric():
                return False
            if not (2020 <= int(v) <= 2030):
                return False
        elif k == "hgt":
            if v[-2:] == "cm":
                if not v[:-2].isnumeric():
                    return False
                if not (150 <= int(v[:-2]) <= 193):
                    return False
            elif v[-2:] == "in":
                if not v[:-2].isnumeric():
                    return False
                if not (59 <= int(v[:-2]) <= 76):
                    return False
            else:
                return False
        elif k == "hcl":
            if v[0] != "#":
                return False
            if not all(c in string.hexdigits for c in v[1:]):
                return False
        elif k == "ecl":
            if v not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
        elif k == "pid":
            if len(v) != 9:
                return False
    return True


def part1(dicts):
    res = 0
    for d in dicts:
        if keys_present(d):
            res += 1
    return res


def part2(dicts):
    res = 0
    for d in dicts:
        if is_valid(d):
            res += 1
    return res


if __name__ == "__main__":
    trees = []
    with open("04/input.txt") as f:
        trees = parse_input(f.read())
    print(part1(trees))
    print(part2(trees))
