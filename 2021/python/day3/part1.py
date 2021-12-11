"""
Module to solve part 1 of day 3 advent of code 2021.
"""
from pathlib import Path
from os import chdir


def main():
    """Main function."""
    path_to_file = Path("../../docs/day3/data.dat")
    with open(path_to_file, "r") as file:
        lines = file.read().splitlines()

    half_signals = len(lines) / 2
    counter = [0] * len(lines[0])
    gamma_rate = ""
    epsilon_rate = ""
    for line in lines:
        for index, digit in enumerate(list(line)):
            counter[index] += int(digit)

    for count in counter:
        if count > half_signals:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    print(gamma_rate, epsilon_rate)
    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])

    chdir(EXEC_DIR)

    main()
