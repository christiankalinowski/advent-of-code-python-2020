from read_functions import read_resources

seat_type = {
    'FLOOR': '.',
    'SEAT_EMPTY': 'L',
    'SEAT_OCCUPIED': '#',
}
seat_type_inv = {val: key for key, val in seat_type.items()}
directions = {
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
}


def get_next_seat_floor(seats, r_idx, s_idx, max_neighbors, neighbor_fn):
    return seat_type['FLOOR']


def get_adjacent_seats(seats: list, r_idx, s_idx):
    return [
        seats[r_idx + d[0]][s_idx + d[1]]
        for d in directions
        if 0 <= r_idx + d[0] < len(seats) and 0 <= s_idx + d[1] < len(seats[r_idx + d[0]])
    ]


def find_seat_in_direction(seats, r_idx, s_idx, d):
    while True:
        r_idx += d[0]
        s_idx += d[1]
        if not(0 <= r_idx < len(seats) and 0 <= s_idx < len(seats[r_idx])):
            return None
        seat = seats[r_idx][s_idx]
        if seat in {seat_type['SEAT_OCCUPIED'], seat_type['SEAT_EMPTY']}:
            return seat


def get_adjacent_seats_direction(seats, r_idx, s_idx):
    return [find_seat_in_direction(seats, r_idx, s_idx, d) for d in directions]


def get_next_seat_seat_empty(seats, r_idx, s_idx, max_neighbors, neighbor_fn):
    adjacent_seats = neighbor_fn(seats, r_idx, s_idx)
    occupied_count = adjacent_seats.count(seat_type['SEAT_OCCUPIED'])
    if occupied_count == 0:
        return seat_type['SEAT_OCCUPIED']
    else:
        return seat_type['SEAT_EMPTY']


def get_next_seat_seat_occupied(seats, r_idx, s_idx, max_neighbors, neighbor_fn):
    adjacent_seats = neighbor_fn(seats, r_idx, s_idx)
    occupied_count = adjacent_seats.count(seat_type['SEAT_OCCUPIED'])
    if occupied_count >= max_neighbors:
        return seat_type['SEAT_EMPTY']
    else:
        return seat_type['SEAT_OCCUPIED']


get_next_seat_def = {
    'FLOOR': get_next_seat_floor,
    'SEAT_EMPTY': get_next_seat_seat_empty,
    'SEAT_OCCUPIED': get_next_seat_seat_occupied,

}


def get_next_seat(seats, r_idx, s_idx, max_neighbors, neighbor_fn):
    seat = seat_type_inv[seats[r_idx][s_idx]]
    return get_next_seat_def[seat](seats, r_idx, s_idx, max_neighbors, neighbor_fn)


def get_next_seats(seats, max_neighbors, neighbor_fn):
    return [
        [get_next_seat(seats, r_idx, s_idx, max_neighbors, neighbor_fn) for s_idx, seat in enumerate(row)]
        for r_idx, row in enumerate(seats)
    ]


def solve():
    seats = read_resources(__file__)

    adjacent_count = get_occupied_seats_on_stable(seats, 4, get_adjacent_seats)
    direction_count = get_occupied_seats_on_stable(seats, 5, get_adjacent_seats_direction)

    return adjacent_count, direction_count


def get_occupied_seats_on_stable(seats, max_neighbors, neighbor_fn):
    while True:
        next_seats = get_next_seats(seats, max_neighbors, neighbor_fn)
        if next_seats == seats:
            break
        else:
            seats = next_seats
    return sum([s.count(seat_type['SEAT_OCCUPIED']) for s in seats])


print(solve())
