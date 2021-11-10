ship_types = {
    "CARRIER": "C",
    "BATTLESHIP": "B",
    "CRUISER": "R",
    "SUBMARINE": "S",
    "DESTROYER": "D"
}

ships_and_lengths = {
    "CARRIER": 5,
    "BATTLESHIP": 4,
    "CRUISER": 3,
    "SUBMARINE": 3,
    "DESTROYER": 2
}

BLANK_SPACE = "_"

HORIZONTAL = 0
VERTICAL = 0
ROW_SIZE = 10
COL_SIZE = 10


def get_base_matrix():
    return [["_"] * 10 for _ in range(10)]
