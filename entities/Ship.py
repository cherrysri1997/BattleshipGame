from entities.Coordinate import Coordinate
from utilities.data_util import ship_types


class Ship:
    # name = ""
    # representation = ""
    # size = 0
    # no_of_hits = 0
    # coordinate: Coordinate = None

    def __init__(self, name: str, size: int, coordinate: Coordinate):
        self.name = name
        self.representation = ship_types[name.upper()]
        self.size = size
        self.coordinate = coordinate
        self.no_of_hits = 0

    def is_ship_sunk(self) -> bool:
        if self.no_of_hits == self.size:
            return True
        return False

    def hit_ship(self) -> bool:
        if not self.is_ship_sunk():
            self.no_of_hits += 1
            return True
        return False
