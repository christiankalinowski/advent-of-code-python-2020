from functools import reduce

from read_functions import read_resources


def solve():
    inputs = read_resources(__file__, "\n\n")
    return (
        sum(map(count_unique_answers, inputs)),
        sum(map(count_common_answers, inputs))
    )


def count_common_answers(answers: str) -> int:
    rows = answers.split("\n")
    intersection = reduce(lambda a, b: set(a) & set(b), rows, set(rows[0]))
    return len(intersection)


def count_unique_answers(answers: str) -> int:
    return len(set(answers.replace("\n", "")))


print(solve())
