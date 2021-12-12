"""
Module to solve part 1 of day 4 advent of code 2021.
"""
from pathlib import Path
from os import chdir
from typing import TextIO


def parse_file(file: TextIO) -> dict:
    """Parses file to create data structures for problem."""
    return file


def main():
    """Main function."""
    path_to_file = Path("../../docs/day4/data.dat")
    with open(path_to_file, "r") as file:
        data = parse_file(file)


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])

    chdir(EXEC_DIR)

    main()
