import re

from read_functions import read_resources

required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
passport = re.compile(r"(\w+):(\S+)")
year = re.compile(r"(\d{4})")
height = re.compile(r"(\d+)(in|cm)")
hcl = re.compile(r"(#[0-9a-f]{6})")
ecl = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)")
pid = re.compile(r"(\d{9})")


def solve():
    inputs = read_resources(__file__, "\n\n")
    passports = list(map(parse_input, inputs))
    all_fields = list(filter(has_all_fields, passports))
    valid = list(filter(is_valid_passport, passports))
    return len(all_fields), len(valid)


def parse_input(input_data) -> dict:
    match = passport.findall(input_data)
    return dict(match)


def has_all_fields(passport: dict) -> bool:
    for field in required_fields:
        if field not in passport:
            return False
    return True


def is_valid_passport(passport: dict) -> bool:
    return has_all_fields(passport) and all([
        is_valid_year(passport['byr'], 1920, 2002),
        is_valid_year(passport['iyr'], 2010, 2020),
        is_valid_year(passport['eyr'], 2020, 2030),
        is_valid_height(passport['hgt']),
        hcl.fullmatch(passport['hcl']) is not None,
        ecl.fullmatch(passport['ecl']) is not None,
        pid.fullmatch(passport['pid']) is not None,
    ])


def is_valid_year(field, low, high) -> bool:
    byr = year.fullmatch(field)
    return byr is not None and low <= int(field) <= high


def is_valid_height(field) -> bool:
    hgt = height.fullmatch(field)
    if hgt is None:
        return False
    value = int(hgt.groups()[0])
    unit = hgt.groups()[1]
    return unit == 'cm' and 150 <= value <= 193 or unit == 'in' and 59 <= value <= 76


print(solve())
