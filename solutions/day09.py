from itertools import combinations
from typing import Optional

from read_functions import read_resources


def solve():
    preamble_length = 25

    inputs = read_resources(__file__)
    numbers = [int(n) for n in inputs]

    working_list = numbers[:preamble_length]

    invalid_number = None
    for number in numbers[preamble_length:]:
        if is_valid(number, working_list):
            del working_list[0]
            working_list.append(number)
        else:
            invalid_number = number
            break

    weakness = None
    for idx, _ in enumerate(numbers):
        weakness = find_weakness(invalid_number, numbers[idx:])
        if weakness is not None:
            break

    return invalid_number, weakness


def is_valid(number, working_list) -> bool:
    return any([sum(item) == number for item in combinations(working_list, 2)])


def find_weakness(target_sum, numbers) -> Optional[int]:
    s = 0
    result = None
    for idx, n in enumerate(numbers):
        s += n
        if s == target_sum:
            result = min(numbers[:idx]) + max(numbers[:idx])
            break
        elif s > target_sum:
            break
    return result


print(solve())
