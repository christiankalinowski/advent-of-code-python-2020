from read_functions import read_resources


def solve():
    line = read_resources(__file__)[0]
    numbers = [int(i) for i in line.split(',')]
    numbers_dict = dict((i, idx + 1) for idx, i in enumerate(numbers))

    i = len(numbers)
    queue = (numbers[-1], i)
    del numbers_dict[numbers[-1]]

    r1 = None

    while i < 30000000:
        n = i - numbers_dict.get(queue[0], i)
        numbers_dict[queue[0]] = queue[1]
        i += 1
        queue = (n, i)
        if queue[1] == 2020:
            r1 = queue[0]

    r2 = queue[0]

    return r1, r2


print(solve())
