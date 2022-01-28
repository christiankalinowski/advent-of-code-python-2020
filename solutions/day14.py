import re

from read_functions import read_resources

mask_pattern = re.compile(r'^mask = ([X10]+)$')
mem_pattern = re.compile(r'^mem\[(\d+)\] = (\d+)$')


def mask_value(value, active_mask):
    s = format(value, 'b').rjust(len(active_mask), '0')
    s = [
        '1' if mask == '1' or mask == 'X' and s[idx] == '1'
        else '0'
        for idx, mask in enumerate(active_mask)
    ]
    return int(''.join(s), 2)


def mask_address(value, active_mask):
    s = format(value, 'b').rjust(len(active_mask), '0')
    s = [''.join([
        s[idx] if mask == '0'
        else mask
        for idx, mask in enumerate(active_mask)
    ])]
    results = []
    while len(s) > 0:
        item = s.pop()
        if item.find('X') >= 0:
            s += [item.replace('X', '1', 1), item.replace('X', '0', 1)]
        else:
            results.append(item)

    return [int(i, 2) for i in results]


def solve():
    inputs = read_resources(__file__)

    active_mask = ''
    mem = {}
    mem2 = {}

    for line in inputs:
        match = mask_pattern.match(line)
        if match is not None:
            active_mask = match.groups()[0]
        match = mem_pattern.match(line)
        if match is not None:
            address, value = match.groups()
            mem[address] = mask_value(int(value), active_mask)

    for line in inputs:
        match = mask_pattern.match(line)
        if match is not None:
            active_mask = match.groups()[0]
        match = mem_pattern.match(line)
        if match is not None:
            address, value = match.groups()
            addresses = mask_address(int(address), active_mask)
            for a in addresses:
                mem2[a] = int(value)

    return sum(mem.values()), sum(mem2.values())


print(solve())
