from typing import List

from utilities.ship_util import is_ship_sunk, hit_ship
from entities.Coordinate import Coordinate
from entities.Player import Player
from entities.Game import Game
from entities.Ship import Ship
from utilities.board_util import print_both_boards
from utilities.coordinate_util import get_coordinate_for_firing
from typing import Dict


def print_notes(notes_repo: List[str], player_A_matrix: List[List[str]], player_B_matrix: List[List[str]]):
    print("\n\nHere is the gameplay:")
    print("---------------------------------\n\n")
    for index, notes in enumerate(notes_repo):
        print(index + 1, ")", notes)

    print_both_boards(player_A_matrix, player_B_matrix)


def note_game_play(notes_repo: List, statement):
    notes_repo.append(statement)


def note_move(notes_repo: List, player_name: str, move: str, is_hit: bool):
    hit_or_miss = "a MISS"
    if is_hit is True:
        hit_or_miss = "a HIT"
    note_game_play(notes_repo, f"{player_name} fired at {move} on the opponent's board and its {hit_or_miss}.")


def is_hit_or_miss(coordinate: Coordinate, opponent: Player):
    if opponent.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] in "!^":
        raise ValueError("Already fired at this co-ordinate previously")

    if opponent.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] == "_":
        opponent.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] = "!"
        opponent.board.abstract_board[coordinate.coordinate_x][coordinate.coordinate_y] = "!"
        return False
    else:
        if hit_ship(opponent.board.ships[opponent.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y]]) is True:
            print(f"{opponent.name}: You have sunk my "
                  f"{opponent.board.ships[opponent.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y]].name}")
        opponent.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] = "^"
        opponent.board.abstract_board[coordinate.coordinate_x][coordinate.coordinate_y] = "^"
        return True


def set_move_on_board(move: Coordinate, player: Player, opponent: Player):

    # print(move)

    if is_hit_or_miss(move, opponent) is True:
        print(f"{opponent.name}: Its a hit, {player.name}!\n")
        return True

    print(f"{opponent.name}: Its a miss, {player.name}!\n")
    return False


def announce_winner_and_loser(winner_name: str, loser_name: str, notes_repo: List[str]):
    statement = f"\n\n{winner_name} has won the game and destroyed the Fleet of {loser_name}!!!\n\n"
    note_game_play(notes_repo, statement)
    print(statement)


def get_winner_and_loser(game: Game) -> bool:

    def are_all_ships_sunk(player_ships: Dict[str, Ship]) -> bool:
        for ship_repr, ship in player_ships.items():
            if is_ship_sunk(ship) is False:
                return False
        return True

    are_player_A_ships_sunk, are_player_B_ships_sunk = \
        are_all_ships_sunk(game.players[0].board.ships), are_all_ships_sunk(game.players[1].board.ships)

    if are_player_A_ships_sunk is True or are_player_B_ships_sunk is True:
        game.active = False
        game.winner, game.loser = (game.players[1], game.players[0]) if are_player_A_ships_sunk is True else (game.players[0], game.players[1])
        # announce_winner_and_loser(game.winner.name, game.loser.name)
        return True

    return False


def get_move(player: Player, opponent: Player):
    def provide_options() -> str:
        print(f"{player.name}, its your turn to chose an option.\n"
              f"Enter 1 to visualize current state of your board and opponent board as well\n"
              f"Enter 2 to Fire on {opponent.name}'s Fleet\n")

        while True:
            option = input("Your option? (1/2): ").strip()

            if option != "1" and option != "2":
                print("Please provide your input as a single digit (1/2). Follow the above instructions.")
            else:
                return option

    opted_for = provide_options()

    if opted_for == "1":
        print_both_boards(player.board.matrix, opponent.board.abstract_board)
    else:
        while True:
            cell_address = input(f"Enter a cell address in the format of [A-J][1-10] to fire at {opponent.name}'s Fleet: ")
            coordinate = get_coordinate_for_firing(cell_address, opponent.board.matrix)

            if coordinate is not None:
                return coordinate


def begin_game(game: Game) -> tuple[Player, Player]:
    turn = True
    # If turn is True then its player_A's turn to open fire
    # else if turn is False then its player_B's turn to open fire.

    while game.active is True:
        if turn is True:
            player, opponent = game.players[0], game.players[1]
        else:
            player, opponent = game.players[1], game.players[0]

        coordinate = get_move(player, opponent)

        if coordinate is not None:
            note_move(game.game_play, player.name,
                      coordinate.input_coordinate, set_move_on_board(coordinate, player, opponent))
            get_winner_and_loser(game)

            turn = not turn

    return game.winner, game.loser
