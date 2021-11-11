from entities.Board import Board


class Player:
    id: int = 1

    def __init__(self, name: str, board: Board):
        self.name: str = name
        self.board: Board = board
        self.id: int = Player.id
        Player.id += 1
