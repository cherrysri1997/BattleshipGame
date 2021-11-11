from entities.Ship import Ship


def is_ship_sunk(ship: Ship) -> bool:
    if ship.no_of_hits >= ship.size:
        return True
    return False


def hit_ship(ship: Ship) -> bool:
    ship.no_of_hits += 1
    if is_ship_sunk(ship):
        return True
    return False
