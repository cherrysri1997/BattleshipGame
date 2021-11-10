from entities.Board import Board


class Player:
    id: int = 1

    def __init__(self, name: str, board: Board):
        self.name = name
        self.board = board
        self.id = Player.id
        Player.id += 1
