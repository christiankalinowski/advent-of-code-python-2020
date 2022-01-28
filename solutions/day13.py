from read_functions import read_resources


def solve():
    inputs = read_resources(__file__)
    estimate = int(inputs[0])
    bus_ids = [(idx, int(bus_id)) for idx, bus_id in enumerate(inputs[1].split(',')) if bus_id != 'x']

    minimum = (-1, estimate)
    step = 1
    i = 0

    for offset, bus_id in bus_ids:
        waiting_time = bus_id - (estimate % bus_id)
        if waiting_time < minimum[1]:
            minimum = (bus_id, waiting_time)

        while True:
            i += step
            if (i + offset) % bus_id == 0:
                step = step * bus_id
                break

    return minimum[0] * minimum[1], i


print(solve())
