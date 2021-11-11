from entities.Board import Board
from typing import List
from utilities.data_util import ROW_SIZE, COL_SIZE


def print_board(matrix_board):
    print("    1  2  3  4  5  6  7  8  9  10")
    print("----------------------------------")
    for index, row in enumerate(matrix_board):
        print(chr(index + 65) + "|  ", end="")

        for column in row:
            print(column, end="  ")

        print()
    print()


def print_both_boards(board: List[List[str]], abstract_board_of_opponent: List[List[str]]):
    print("On the left is the current state of your board and"
          "on the other side is the current state of your opponent's board.\n"
          "'_' indicates this place hasn't be fired yet,\n"
          "'!' indicates that it is a miss-fire\n"
          "'^' indicates that it is a hit\n")
    print("    1  2  3  4  5  6  7  8  9  10                1  2  3  4  5  6  7  8  9  10")
    print("-----------------------------------        ------------------------------------")
    for row in range(ROW_SIZE):
        print(chr(row + 65) + "|  ", end="")

        for col in range(COL_SIZE):
            print(board[row][col], end="  ")

        print("           ", end="")
        print(chr(row + 65) + "|  ", end="")

        for col in range(COL_SIZE):
            print(abstract_board_of_opponent[row][col], end="  ")

        print()
    print()


def set_ship_on_board(matrix_board, ship):
    if ship.coordinate.arrangement_type == 0:
        for cols in range(ship.coordinate.coordinate_y, ship.coordinate.coordinate_y + ship.size):
            matrix_board[ship.coordinate.coordinate_x][cols] = ship.representation
    else:
        for rows in range(ship.coordinate.coordinate_x, ship.coordinate.coordinate_x + ship.size):
            matrix_board[rows][ship.coordinate.coordinate_y] = ship.representation

    print_board(matrix_board)


# def set_abstract_board(board: Board):
#     for row in range(len(board.matrix)):
#         for col in range(len(board.matrix[0])):
#             if board.matrix[row][col] == "!" or board.matrix[row][col] == "^":
#                 board.abstract_board[row][col] = board.matrix[row][col]
