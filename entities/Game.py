from entities.Player import Player
from typing import List


class Game:
    id = 1

    def __init__(self, playerA: Player, playerB: Player):
        self.id: int = Game.id
        Game.id += 1
        self.players: List[Player] = [playerA, playerB]
        self.game_play: List[str] = []
        self.winner: Player or None = None
        self.loser: Player or None = None
        self.active: bool = True
        # self.disrupted: bool = False
