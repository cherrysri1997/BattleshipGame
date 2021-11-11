from entities.Board import Board
from entities.Player import Player
from entities.Ship import Ship
from utilities.coordinate_util import get_coordinate
from utilities.board_util import print_board, set_ship_on_board
from utilities.data_util import ship_types, ships_and_lengths, get_base_matrix


def get_player(player_name, matrix_board) -> Player:
    print(f"\n{player_name}, you have to place your 5 ships on the boards. Please enter valid inputs based on the "
          f"following conditions:")

    ships_details = f"SHIP_NAME   SHIP_SIZE   SHIP_REPRESENTATION\n"
    ships_details += "-" * 45 + "\n"

    for key in ship_types.keys():
        ships_details += key.ljust(12) + str(ships_and_lengths[key]).rjust(5) + ship_types[key].rjust(14) + "\n"

    print("There are 5 ships and each of the ship has a certain length mentioned in the brackets, also each ship is "
          "represented by a character as shown below (separated by hyphen):\n" + ships_details)

    print("The input format for each ship must be in: [A-J][1-10][0-1].\n[A-J] represent rows on the board,\n"
          "[1-10] represent columns on the board and\n[0-1] represents alignment type of the ship i.e., "
          "Horizontal(0)/Vertical(1).\n\nExample for a valid input: B101. Here, 'B' is second row, '10' is 10th column "
          "and '1' is vertical alignment.\n\nIf you want to place a ship horizontally(0) then enter the value of "
          "left-most cell, whereas, to place a ship vertically(1) enter the value of top-most cell.")

    print("Suppose you want to place the Carrier(5) vertically on the column '1' and starting from row H, it is not "
          "possible because the available space on column '1' from row 'H' - 'J' is 3 cells but required space for a "
          "Carrier to fit is 5. An empty board will be shown for better visualization.\nDo not worry much about "
          "invalid inputs, because you will be prompted if you do so.\n")

    print_board(matrix_board)

    print("Please provide inputs for the ships being prompted for:")

    ships_and_placements = {}
    player_board_matrix = get_base_matrix()

    for ship_name, ship_length in ships_and_lengths.items():
        while True:
            cell_address = input(f"Enter the cell address for {ship_name} ({ship_length}) - {ship_types[ship_name]}: ")
            coordinate = get_coordinate(cell_address, player_board_matrix, ship_length)

            if coordinate is not None:
                ships_and_placements[ship_types[ship_name]] = Ship(ship_name, ship_length, coordinate)
                set_ship_on_board(player_board_matrix, ships_and_placements[ship_types[ship_name]])
                break
            else:
                print("Please provide valid input! Follow the above mentioned instructions. Here's the board for the "
                      "benefit of visualization:\n")
                print_board(player_board_matrix)

    player_board = Board(player_board_matrix)
    player_board.set_ships(ships_and_placements)

    return Player(player_name, player_board)


def get_player_names():
    player_name_A = input("Enter name of first player: ")

    while len(player_name_A) < 4:
        player_name_A = input("Enter name of first player (Please enter at least 4 characters): ")

    player_name_B = input("Enter name of second player: ")

    while len(player_name_B) < 4:
        player_name_B = input("Enter name of second player (Please enter at least 4 characters): ")

    return player_name_A, player_name_B


def choose_player_to_begin(player_A: Player, player_B: Player) -> tuple:

    """
    This utility function decides which player to start the match.
    If it returns 0, then Player_A starts the game
    If it returns 1, then Player_B starts the game

    :param player_A: Player
    :param player_B: Player
    :return: 0/1 int
    """

    def choose_player_util(player_name):
        while True:
            player_input = input(f"\n\n{player_name}, please choose one between ODD/EVEN (respond with o/e "
                                 f"respectively, case insensitive): ")
            if player_input.upper() in "OE" and len(player_input) == 1:
                return player_input.upper()
            else:
                print("Please enter valid input.\n")

    def choose_number(player_name) -> int:
        while True:
            player_input = input(f"{player_name}, chose an integer between 1 and 10 (inclusive): ")
            if player_input.isnumeric() and 1 <= int(player_input) <= 10:
                return int(player_input)
            else:
                print("Please enter valid input.\n")

    def decide_winner() -> bool:
        _sum = sum((player_A_num, player_B_num))
        if (_sum % 2 == 0 and player_A_input == "E") or (_sum % 2 == 1 and player_A_input == "O"):
            return True
        return False

    player_A_input = choose_player_util(player_A.name)
    # player_B_input = choose_player_util(player_B.name)

    player_A_num = choose_number(player_A.name)
    player_B_num = choose_number(player_B.name)

    if decide_winner() is True:
        return player_A, player_B

    return player_B, player_A


def show_toss_winner(toss_winner: Player):
    print(f"{toss_winner.name} has won the toss and gets a chance to FIRE first.\n")
