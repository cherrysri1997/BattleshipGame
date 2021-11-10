from entities.Ship import Ship
from entities.Coordinate import Coordinate
from typing import Dict, List

from utilities.data_util import get_base_matrix


class Board:
    # Structure of the member "ships" is:
    #             {
    #                 "C": Ship,
    #                 "B": Ship,
    #                 "R": Ship,
    #                 "S": Ship,
    #                 "D": Ship
    #             }

    def __init__(self, matrix: List[List[str]]):
        self.matrix = matrix
        self.abstract_board = get_base_matrix()
        self.ships = None  # ships: Dict[str, Ship]

    def set_ships(self, ships: Dict[str, Ship]):
        self.ships = ships


    def set_hit_or_miss(self, coordinate: Coordinate):
        if self.matrix[coordinate.coordinate_x][coordinate.coordinate_y] == "_":  # '!' denotes a Miss
            self.matrix[coordinate.coordinate_x][coordinate.coordinate_y] = "!"
        else:  # '^' denotes a hit
            self.matrix[coordinate.coordinate_x][coordinate.coordinate_y] = "^"
