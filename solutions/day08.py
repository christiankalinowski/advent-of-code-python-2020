from read_functions import read_resources
import re

pattern = re.compile(r"(\w+) ([+-]\d+)")

ops = {
    "nop": lambda acc, pos, val: (acc, pos + 1),
    "jmp": lambda acc, pos, val: (acc, pos + val),
    "acc": lambda acc, pos, val: (acc + val, pos + 1)
}
replacements = {
    "nop": "jmp",
    "jmp": "nop",
    "acc": "acc"
}


def solve():
    inputs = read_resources(__file__)
    instructions = list(map(lambda r: pattern.fullmatch(r).groups(), inputs))

    acc, _ = run(instructions)

    acc_success = -1
    for idx, ins in enumerate(instructions):
        new_ins = (replacements[ins[0]], ins[1])
        new_instructions = [new_ins if x == ins else x for x in instructions]
        res, success = run(new_instructions)
        if success:
            acc_success = res
            break

    return acc, acc_success


def run(instructions):
    acc = pos = 0
    visited_pos = [len(instructions)]
    while pos not in visited_pos:
        visited_pos.append(pos)
        ins, val = instructions[pos]
        acc, pos = ops[ins](acc, pos, int(val))
    return acc, len(instructions) == pos


print(solve())
