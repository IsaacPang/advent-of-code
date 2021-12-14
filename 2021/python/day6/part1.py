"""
Module to solve part 1 of day 6 advent of code 2021.
"""
from pathlib import Path
from os import chdir


def main():
    """Main function."""


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])
    chdir(EXEC_DIR)
    main()
