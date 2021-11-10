from entities.Player import Player
from entities.Coordinate import Coordinate
from typing import List


# Shift this function to Utils Class, further
def note_move(notes_repo: List, player_name: str, move: str, is_hit: bool):
    hit_or_miss = "an INVALID COORDINATE"
    if is_hit is True:
        hit_or_miss = "a HIT"
    elif is_hit is None:
        hit_or_miss = "a MISS"
    notes_repo.append(f"{player_name} fired at {move} on the opponent's board and its {hit_or_miss}.")


# Shift this function to Utils Class, further
def is_hit_or_miss(player: Player, coordinate: Coordinate):
    if player.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] in "!^":
        raise ValueError("Already fired at this co-ordinate previously")
    if player.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] == "_":
        player.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] = "!"
        return False
    else:
        player.board.ships[player.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y]].hit_ship()
        player.board.matrix[coordinate.coordinate_x][coordinate.coordinate_y] = "^"
        return True


class Game:
    id = 1

    def __init__(self, playerA: Player, playerB: Player):
        self.id, Game.id = Game.id, Game.id + 1
        self.players: List[Player] = [playerA, playerB]
        self.game_play = []
        self.winner = None
        self.loser = None
        self.active = True
        self.disrupted = False

    def set_board(self, player: Player, move: Coordinate):
        is_hit = None
        try:
            is_hit = is_hit_or_miss(player, move)
        except ValueError as e:
            return str(e)
        finally:
            note_move(self.game_play, player.name, move.input_coordinate, is_hit)
