"""
Module to solve part 1 of day 4 advent of code 2021.
"""
from pathlib import Path
from os import chdir
from typing import TextIO, Union
import json
from collections import Counter


class BingoBoard:
    """Bingo board with 5 rows and 5 columns."""

    class BingoNumber:
        """Number on bingo board."""

        __slots__ = "row", "col", "value"

        def __init__(self, row_index, col_index, value):
            self.row = row_index
            self.col = col_index
            self.value = int(value)

        def json(self):
            """Return a dictionary to allow for json serialisation."""
            return {key: getattr(self, key) for key in self.__slots__}

    def __init__(self, rows):
        self.numbers = {
            num: BingoBoard.BingoNumber(row_index, col_index, num)
            for row_index, row in enumerate(rows, 1)
            for col_index, num in enumerate(row, 1)
        }
        self.marked_numbers = []
        self.win = False
        self.last_called = None

    def __str__(self):
        return json.dumps(
            {num: val.json() for num, val in self.numbers.items()},
            indent=4,
            default=vars,
        )

    def check_row_bingo(self):
        """Check the rows of the board for bingo."""
        marked_rows = Counter([num.row for num in self.marked_numbers])
        if any(value == 5 for value in marked_rows.values()):
            self.win = True

    def check_col_bingo(self):
        """Check the cols of the board for bingo."""
        marked_cols = Counter([num.col for num in self.marked_numbers])
        if any(value == 5 for value in marked_cols.values()):
            self.win = True

    def mark(self, number: str):
        """Mark a number on the board."""
        self.last_called = int(number)
        if number in self.numbers:
            self.marked_numbers.append(self.numbers.pop(number))
            self.check_row_bingo()
            self.check_col_bingo()

    def calc_score(self):
        """Calculate the score of the board."""
        if self.win:
            unmarked_sum = sum([num.value for num in self.numbers.values()])
            return self.last_called * unmarked_sum
        return 0


def parse_file(file: TextIO) -> dict:
    """Parses file to create data structures for this problem."""
    draws = next(file).strip("\n").split(",")
    board_rows = []
    boards = []
    line_counter = 0

    def clean_line(line):
        as_list = line.strip("\n").split(" ")
        return [digit.strip() for digit in as_list if digit.strip()]

    for line in file:
        line_counter += 1
        if line_counter > 1:
            board_rows.append(clean_line(line))

        if line_counter == 6:
            boards.append(BingoBoard(board_rows))
            board_rows = []
            line_counter = 0

    return draws, boards


def mark_all_boards(draw: str, boards: list) -> Union[None, int]:
    """Mark all boards and get the max score if a board wins."""
    for board in boards:
        board.mark(draw)
        if board.win:
            return board.calc_score()

    return None


def first_win_score(draws: list, boards: list) -> int:
    """Returns the score of the first board to win."""
    for draw in draws:
        curr_score = mark_all_boards(draw, boards)
        if curr_score:
            return curr_score

    return None


def main():
    """Main function."""
    path_to_file = Path("../../docs/day4/data.dat")
    with open(path_to_file, "r") as file:
        draws, boards = parse_file(file)

    print(first_win_score(draws, boards))  # 2496


if __name__ == "__main__":
    EXEC_FILEPATH = str(Path(__file__))
    EXEC_DIR = "/".join(EXEC_FILEPATH.split("/")[:-1])

    chdir(EXEC_DIR)

    main()
