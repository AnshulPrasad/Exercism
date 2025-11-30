"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for i in range(number):
        yield "ABCD"[i % 4]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row_num = 1
    seat_letter_sequence = generate_seat_letters(number)

    if number > 12 * 4:  # row number 13 is encountered.
        number += 4

    t = 1  # to count number of iteration to skip on seat number 13
    for i in range(1, number + 1):
        if row_num == 13 and t < 5:
            t += 1
            if t == 5:
                row_num += 1
            continue

        yield str(row_num) + next(seat_letter_sequence)

        if i % 4 == 0:
            row_num += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    ans = {}
    seats = generate_seats(len(passengers))
    for i in passengers:
        ans[i] = next(seats)

    return ans


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    for i in seat_numbers:
        yield f"{i}{flight_id}{'0'*12}"[:12]
