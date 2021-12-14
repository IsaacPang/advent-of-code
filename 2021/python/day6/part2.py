"""
Module to solve part 2 of day 6 advent of code 2021.
"""
from pathlib import Path
from os import chdir


def decrease_one(value: int) -> int:
    """Decrement an int by one."""
    return value - 1


def main():
    """Main function."""
    path_to_file = Path("../../docs/day6/data.dat")
    with open(path_to_file, "r") as file:
        fishes = [int(value) for value in file.read().strip("\n").split(",")]

    days_after = 0
    fishes_to_add = []
    while days_after < 80:
        fishes += fishes_to_add
        fishes_to_add = []
        fishes = [decrease_one(fish) for fish in fishes]
        for index, fish in enumerate(fishes):
            if fish == 0:
                fishes[index] = 7
                fishes_to_add.append(9)
        days_after += 1

    print(len(fishes))


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])
    chdir(EXEC_DIR)
    main()
