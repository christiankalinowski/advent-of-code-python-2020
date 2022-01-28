from read_functions import read_resources


def solve():
    inputs = read_resources(__file__)
    numbers = [int(n) for n in inputs]

    built_in_adapter_jolt = max(numbers) + 3
    adapters = [*numbers, built_in_adapter_jolt]

    jolt = 0
    jolt_diffs = {1, 2, 3}
    jolt_diffs_count = {1: 0, 2: 0, 3: 0}

    while jolt < built_in_adapter_jolt:
        for diff in jolt_diffs:
            if jolt + diff in adapters:
                jolt += diff
                jolt_diffs_count[diff] += 1
                break

    jolt = 0
    arrangements = {0: 1}
    while jolt < built_in_adapter_jolt:
        for diff in jolt_diffs:
            if jolt + diff in adapters:
                arrangements[jolt + diff] = arrangements.get(jolt + diff, 0) + arrangements[jolt]
        del arrangements[jolt]
        jolt = min(arrangements.keys())

    return jolt_diffs_count[1] * jolt_diffs_count[3], sum(arrangements.values())


print(solve())
