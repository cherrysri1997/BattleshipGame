from entities.Coordinate import Coordinate
from utilities.data_util import ship_types


class Ship:

    def __init__(self, name: str, size: int, coordinate: Coordinate):
        self.name: str = name
        self.representation: str = ship_types[name.upper()]
        self.size: int = size
        self.coordinate: Coordinate = coordinate
        self.no_of_hits: int = 0
