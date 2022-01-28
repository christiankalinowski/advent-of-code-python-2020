import numpy as np

from read_functions import read_resources

Vector = np.array

compass = {
    'N': Vector([1, 0]),
    'E': Vector([0, 1]),
    'S': Vector([-1, 0]),
    'W': Vector([0, -1]),
}
directions = list(compass.values())


def solve():
    inputs = read_resources(__file__)
    instructions = [(i[0], int(i[1:])) for i in inputs]

    direction = Vector([0, 1])
    position = Vector([0, 0])

    for d, v in instructions:
        if d in compass:
            position += compass[d] * v
        if d == 'F':
            position += direction * v
        if d == 'L':
            direction = turn(direction, -v)
        if d == 'R':
            direction = turn(direction, v)

    ship_position = Vector([0, 0])
    wp_position = Vector([1, 10])

    for d, v in instructions:
        if d in compass:
            wp_position += compass[d] * v
        if d == 'F':
            ship_position += wp_position * v
        if d == 'L':
            wp_position = rotate(wp_position, v)
        if d == 'R':
            wp_position = rotate(wp_position, -v)

    return sum([abs(p) for p in position]), sum([abs(p) for p in ship_position])


def turn(direction, angle):
    idx = np.where((directions == direction).all(axis=1))[0][0]
    return directions[(idx + angle // 90) % len(directions)]


def rotate(position, angle):
    i = (angle // 90) % 4
    for _ in range(i):
        position = (position[1], position[0] * -1)
    return Vector(position)


print(solve())
