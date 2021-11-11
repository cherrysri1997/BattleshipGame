from utilities.data_util import get_base_matrix
from entities.Game import Game

from utilities.player_util import get_player, get_player_names, choose_player_to_begin, show_toss_winner
from utilities.game_util import begin_game, announce_winner_and_loser, print_notes

if __name__ == '__main__':
    player_A_name, player_B_name = get_player_names()

    empty_board = get_base_matrix()

    player_A = get_player(player_A_name, empty_board)
    player_B = get_player(player_B_name, empty_board)

    player_A, player_B = choose_player_to_begin(player_A, player_B)
    show_toss_winner(player_A)

    game = Game(player_A, player_B)

    winner, loser = begin_game(game)

    announce_winner_and_loser(winner.name, loser.name, game.game_play)

    print_notes(game.game_play, winner.board.matrix, loser.board.matrix)
