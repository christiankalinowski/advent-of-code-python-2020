import operator
from functools import reduce

from read_functions import read_resources


def solve():
    inputs = read_resources(__file__)
    results = [
        calculate_hits(inputs, 1, 1),
        calculate_hits(inputs, 3, 1),
        calculate_hits(inputs, 5, 1),
        calculate_hits(inputs, 7, 1),
        calculate_hits(inputs, 1, 2),
    ]
    return (
        results[1],
        reduce(operator.mul, results, 1)
    )


def calculate_hits(inputs, x_diff, y_diff) -> int:
    row_length = len(inputs[0])
    x = y = hits = 0
    while y < len(inputs):
        if inputs[y][x] == '#':
            hits += 1
        y += y_diff
        x = (x + x_diff) % row_length
    return hits


print(solve())
