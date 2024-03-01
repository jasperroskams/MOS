from dataclasses import dataclass


@dataclass
class GameCoordinate:
    x: int
    y: int

    def __add__(self, other):
        return GameCoordinate(self.x + other.x, self.y + other.y)

