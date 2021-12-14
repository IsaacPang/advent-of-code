"""
Module to solve part 1 of day 5 advent of code 2021.
"""
from pathlib import Path
from os import chdir
from typing import Generator, TextIO
from collections import Counter


# defining the coordinate type
Coordinate = tuple[int]


def parse_coord(coord: str) -> Coordinate:
    """Parses the string coordinates into integer tuples."""
    return tuple(int(val) for val in coord.strip().split(","))


def parse_file(file: TextIO) -> Generator:
    """Returns line by line of file"""
    for line in file:
        yield tuple(
            parse_coord(coordinate) for coordinate in line.strip("\n").split(" -> ")
        )


def get_line(start: Coordinate, end: Coordinate) -> list[Coordinate]:
    """Returns a list of all coordinates between two coordinates.
    Only works for vertical and horizontal lines only"""
    horz1, vert1 = start
    horz2, vert2 = end
    between_horz = range(min(horz1, horz2), max(horz1, horz2) + 1)
    between_vert = range(min(vert1, vert2), max(vert1, vert2) + 1)

    if horz1 == horz2 or vert1 == vert2:
        return [(x, y) for x in between_horz for y in between_vert]
    return []


def main():
    """Main function."""
    path_to_file = Path("../../docs/day5/data.dat")
    # path_to_file = Path("../../docs/day5/test.dat")
    with open(path_to_file, "r") as file:
        straight_lines = []
        for pair in parse_file(file):
            print(pair)
            straight_lines += get_line(*pair)

    positions = Counter(straight_lines)

    print(sum(vals > 1 for vals in positions.values()))


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])
    chdir(EXEC_DIR)
    main()
