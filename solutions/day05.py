from itertools import product

from read_functions import read_resources


def solve():
    inputs = read_resources(__file__)
    seats = list(map(convert, inputs))
    seat_ids = list(map(lambda i: i[0] * 8 + i[1], seats))
    emtpy_seats = set(product(range(128), range(8))) - set(seats)
    empty_seat_ids = list(map(lambda i: i[0] * 8 + i[1], emtpy_seats))

    empty_seat_id = 0
    for seat_id in empty_seat_ids:
        if seat_id + 1 in seat_ids and seat_id - 1 in seat_ids:
            empty_seat_id = seat_id

    return max(*seat_ids), empty_seat_id


def convert(ticket: str):
    row = ticket[:7]
    col = ticket[7:]
    row_base2 = row.replace('F', '0').replace('B', '1')
    col_base2 = col.replace('L', '0').replace('R', '1')
    return int(row_base2, 2), int(col_base2, 2)


print(solve())
