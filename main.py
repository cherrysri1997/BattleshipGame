from utilities.data_util import get_base_matrix
from entities.Game import Game

from utilities.player_util import get_player, get_player_names, choose_player_to_begin

if __name__ == '__main__':
    player_A_name, player_B_name = get_player_names()
    # player_A_name, player_B_name = "Tony", "Peter"

    empty_board = get_base_matrix()

    player_A = get_player(player_A_name, empty_board)
    player_B = get_player(player_B_name, empty_board)

    if choose_player_to_begin(player_A, player_B) == 1:
        player_A, player_B = player_B, player_A

    game = Game(player_A, player_B)
    print(game.players[0].name, game.players[1].name)

    """
        Yet to develop:
        ----------------
        * After creating a game, start the game play and keep noting the moves
        * The user has to be provided with two options every time he/she gets a chance to perform their move:
            1. Option to view the boards (Their own board and the abstract board of the opponent, side-by-side)
            2. Option to make a move.
        * If the user opts for 2nd one, then take input, validate the input, process the input and update the boards
          accordingly. Then show whether its a hit/miss.
        * After each move performed by any player, check whether if anyone has won the game. If yes, then stop the game
          and announce the winner. Then get the acknowledgement from both the users to restart the game
          and act accordingly.
    """
    pass
