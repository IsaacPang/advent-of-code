"""
Module to solve part 2 of day 6 advent of code 2021.
"""
from os import chdir
from collections import Counter
from pathlib import Path


def decrease_one(value: int) -> int:
    """Decrement an int by one."""
    return value - 1


def main():
    """Main function."""
    path_to_file = Path("../../docs/day6/data.dat")
    with open(path_to_file, "r") as file:
        fishes = [int(value) for value in file.read().strip("\n").split(",")]

    fish_counter = dict(Counter(fishes))

    max_day = 256
    for day in range(max_day):
        zero_count_fish = fish_counter.get(0,0)
        fish_counter[0] = fish_counter[1]
        for count in range(1, 8):
            fish_counter[count] = fish_counter.get(count + 1, 0)

        fish_counter[6] += zero_count_fish
        fish_counter[8] = zero_count_fish

    print(sum(fish_counter.values()))

if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])
    chdir(EXEC_DIR)
    main()
