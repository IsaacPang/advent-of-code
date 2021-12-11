"""
Module to solve part 2 of day 2 advent of code 2021.
"""
from pathlib import Path
from os import chdir
from typing import NamedTuple


class Location(NamedTuple):
    """Location named tuple."""

    horizontal_position: int
    depth: int


class Submarine:
    """Submarine class."""

    def __init__(self) -> None:
        self.horz = 0
        self.aim = 0
        self.depth = 0

    def move_forward(self, distance) -> None:
        """Moves the sub forward. Increases horizontal distance and depth depending on aim."""
        self.horz += distance
        self.depth += distance * self.aim

    def aim_up(self, angle) -> None:
        """Aims the sub up. No change in position."""
        self.aim -= angle

    def aim_down(self, angle) -> None:
        """Aims the sub down. No change in position."""
        self.aim += angle

    def move(self, direction, distance) -> None:
        """Moves submarine according to provided direction."""
        direction_mapping = {
            "forward": self.move_forward,
            "up": self.aim_up,
            "down": self.aim_down,
        }
        direction_mapping[direction](distance)

    def get_location(self) -> Location:
        """Returns submarine location based on horizontal position and depth."""
        return Location(self.horz, self.depth)


def main():
    """Main function."""
    path_to_file = Path("../../docs/day2/data.dat")

    with open(path_to_file, "r") as file:
        lines = file.read().splitlines()

    def coerce_int(val: str):
        try:
            return int(val)
        except ValueError:
            return val

    sub = Submarine()
    for instruction in lines:
        direction, units = map(coerce_int, instruction.split())
        sub.move(direction, units)

    location = sub.get_location()

    print(location.horizontal_position * location.depth)


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])

    chdir(EXEC_DIR)

    main()

