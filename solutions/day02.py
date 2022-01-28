import re
from read_functions import read_resources

def solve():
    p = re.compile(r'^(\d+)-(\d+) (\w): (\w+)$')
    inputs = read_resources(__file__)
    parsed = list(map(lambda s: p.match(s).groups(), inputs))
    return [
        len(list(filter(is_valid_password, parsed))),
        len(list(filter(is_valid_password2, parsed)))
    ]


def is_valid_password(params) -> bool:
    min_count, max_count, char, password = params
    count = list(password).count(char)
    return int(min_count) <= count <= int(max_count)


def is_valid_password2(params) -> bool:
    min_count, max_count, char, password = params
    return (password[int(min_count) - 1] == char) != (password[int(max_count) - 1] == char)


print(solve())
