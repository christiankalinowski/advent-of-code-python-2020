from functools import reduce
from itertools import combinations
import operator

from read_functions import read_resources


def solve():
    inputs = read_resources(__file__)
    numbers = list(map(lambda i: int(i), inputs))

    return calculate_result(numbers, 2020, 2), calculate_result(numbers, 2020, 3)


def calculate_result(inputs, sum_value, dept):
    input_combinations = combinations(inputs, dept)
    matches = filter(lambda r: sum(r) == sum_value, input_combinations)
    results = map(lambda r: reduce(operator.mul, r, 1), matches)
    return list(results)[0]


print(solve())
