"""
Module to solve part 1 of day 3 advent of code 2021.
"""
from pathlib import Path
from os import chdir


def reach_target(lines: list, index: int, most_common: bool = True) -> None:
    """Retrieve the gamma and epsilon rates."""
    half_signals = len(lines) / 2
    counter = 0
    for line in lines:
        counter += int(line[index])

    if most_common:
        if counter >= half_signals:
            target = "1"
        else:
            target = "0"
    else:
        if counter < half_signals:
            target = "1"
        else:
            target = "0"

    return [line for line in lines if line[index] == target]


def filter_rating(lines: list, most_common: bool = True) -> str:
    """Filter the data for the oxygen rating."""

    lines_copy = lines.copy()
    index = 0
    while len(lines_copy) != 1:
        lines_copy = reach_target(lines_copy, index, most_common)
        index += 1

    return lines_copy.pop()


def main():
    """Main function."""
    path_to_file = Path("../../docs/day3/data.dat")
    with open(path_to_file, "r") as file:
        lines = file.read().splitlines()

    oxygen_rating = filter_rating(lines)
    co2_rating = filter_rating(lines, most_common=False)

    print(int(oxygen_rating, 2) * int(co2_rating, 2))


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])

    chdir(EXEC_DIR)

    main()
