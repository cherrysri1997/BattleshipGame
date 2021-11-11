from typing import List

from entities.Coordinate import Coordinate
from utilities.data_util import COL_SIZE, HORIZONTAL, BLANK_SPACE, ROW_SIZE


def is_valid_placement(
        cell_address: str,
        with_board: bool = False,
        matrix_board: List[List[str]] = None,
        ship_length: int = None
) -> tuple or None:
    """
    If a given cell address is valid,
    then return the coordinates in a tuple format (x, y, arrangement_type/alignment_type),
    else return None

    :param cell_address: str
    :param matrix_board: List[List[str]]
    :param with_board: To check whether cell_address is valid including a separate check on the board
    :param ship_length: int
    :return: tuple/None
    """

    if 3 <= len(cell_address) <= 4:
        coordinates_tuple = ()
        if cell_address[0].isalpha() and ord("A") <= ord(cell_address[0].upper()) <= ord("J"):
            coordinates_tuple += (ord(cell_address[0].upper()) - ord("A"),)  # 0-indexing
        else:
            print("The row must be an alphabet between A and J (inclusive).")
            return None

        if len(cell_address) == 4:
            if cell_address[1].isdigit() and cell_address[2].isdigit() and 1 <= int(cell_address[1:3]) <= COL_SIZE:
                coordinates_tuple += (int(cell_address[1:3]) - 1,)  # 0-indexing
            else:
                print("The column must be an integer between 1 and 10 (inclusive).")
                return None

            if cell_address[3] in "01":
                coordinates_tuple += (int(cell_address[3]),)
            else:
                print("The alignment must either be 0 (for Horizontal alignment) or 1 (for Vertical alignment)")
                return None
        else:
            if cell_address[1].isdigit() and 1 <= int(cell_address[1]) <= 10:
                coordinates_tuple += (int(cell_address[1]) - 1,)  # 0-indexing
            else:
                print("The column must be an integer between 1 and 10 (inclusive).")
                return None

            if cell_address[2] in "01":
                coordinates_tuple += (int(cell_address[2]),)
            else:
                print("The alignment must either be 0 (for Horizontal alignment) or 1 (for Vertical alignment)")
                return None

        if with_board is True:
            # This part is to check whether a ship is already placed in the cell address space provided.

            if ship_length is None or matrix_board is None:
                print("If you don't want an additional check for board, the 'with_board' argument should be False.")
                return None

            if coordinates_tuple[2] == HORIZONTAL:  # Horizontal
                if ship_length <= COL_SIZE - coordinates_tuple[1]:
                    for cols in range(coordinates_tuple[1], coordinates_tuple[1] + ship_length):
                        if matrix_board[coordinates_tuple[0]][cols] != BLANK_SPACE:
                            print(f"The cell address space has already been occupied by another ship '{matrix_board[coordinates_tuple[0]][cols]}'. See the board for clear understanding.")
                            return None
                else:
                    print(f"Ship size is more than the space available from the selected column. Space available is {COL_SIZE - coordinates_tuple[1]} and ship size is {ship_length}")
                    return None

            else:  # Vertical
                if ship_length <= ROW_SIZE - coordinates_tuple[0]:
                    for rows in range(coordinates_tuple[0], coordinates_tuple[0] + ship_length):
                        if matrix_board[rows][coordinates_tuple[1]] != BLANK_SPACE:
                            print(f"The cell address space has already been occupied by another ship '{matrix_board[rows][coordinates_tuple[1]]}'. See the board for clear understanding.")
                            return None
                else:
                    print(f"Ship size is more than the space available from the selected row. Space available is {ROW_SIZE - coordinates_tuple[0]} and ship size is {ship_length}")
                    return None

        return coordinates_tuple

    else:
        print("The size of the cell address should be 3 or 4 characters. Examples of valid inputs: B51, h100")
        return None


def get_coordinate_for_firing(cell_address: str, matrix: List[List[str]]) -> Coordinate or None:
    input_error_msg = "Please provide valid cell address.\n"
    row_error_msg = "Row address must be in between 'A' and 'J' (inclusive)."
    col_error_msg = "Column address must be in between 1 and 10 (inclusive)."

    coordinate_tuple = tuple()

    if 2 <= len(cell_address) <= 3:
        if cell_address[0].isalpha() and ord("A") <= ord(cell_address[0].upper()) <= ord("J"):
            coordinate_tuple += (ord(cell_address[0].upper()) - ord("A"),)
        else:
            print(row_error_msg, input_error_msg)
            return None

        if len(cell_address) == 3:
            if cell_address[1:] == "10":
                coordinate_tuple += (9,)
            else:
                print(col_error_msg, input_error_msg)
                return None
        else:
            if 1 <= int(cell_address[1]) <= 9:
                coordinate_tuple += (int(cell_address[1]) - 1,)
            else:
                print(col_error_msg, input_error_msg)
                return None

        if matrix[coordinate_tuple[0]][coordinate_tuple[1]] in "!^":
            print(f"The cell address {cell_address} has already been fired!", input_error_msg)
            return None

        # There is no arrangement type for firing coordinate. So pass -1 for the "arrangement_type" arg.
        return Coordinate(coordinate_tuple[0], coordinate_tuple[1], -1, cell_address)
    else:
        print(input_error_msg)
        return None


def get_coordinate(cell_address, matrix_board, ship_length) -> Coordinate or None:
    coordinates_tuple = is_valid_placement(cell_address, True, matrix_board, ship_length)

    if coordinates_tuple is not None:
        return Coordinate(coordinates_tuple[0], coordinates_tuple[1], coordinates_tuple[2], cell_address)
    else:
        return None
