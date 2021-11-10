from entities.Board import Board


def print_board(matrix_board):
    print("    1  2  3  4  5  6  7  8  9  10")
    print("----------------------------------")
    for index, row in enumerate(matrix_board):
        print(chr(index + 65) + "|  ", end="")

        for column in row:
            print(column, end="  ")

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


def set_abstract_board(board: Board):
    for row in range(len(board.matrix)):
        for col in range(len(board.matrix[0])):
            if board.matrix[row][col] == "!" or board.matrix[row][col] == "^":
                board.abstract_board[row][col] = board.matrix[row][col]
