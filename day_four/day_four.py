from pathlib import Path
from typing import Tuple, List

from utils.file import readin_files


class BingoBoard:

    def __init__(self, raw_input: List[List[int]]):
        self.rows: List[List[int]] = []
        self.cols: List[List[int]] = [[-1 for _ in range(5)] for _ in range(5)]
        self.marked_numbers: List[int] = []
        self.used_numbers: List[int] = []
        self.has_won = False
        for row_counter, line in enumerate(raw_input):
            self.rows.append(line)
            self.used_numbers.extend(line)
            for col_counter in range(5):
                self.cols[col_counter][row_counter] = line[col_counter]
        self.all = self.rows
        [self.all.append(line) for line in self.cols]

    def check_for_hit(self, number):
        if number in self.used_numbers:
            self.marked_numbers.append(number)

    def check_for_win(self) -> bool:
        if len(self.marked_numbers) < 5:
            return False

        if self.has_won:
            return True

        for line in self.all:
            if len([x for x in line if x in self.marked_numbers]) == 5:
                self.has_won = True
                return True
        return False

    def calc_wining_score(self) -> int:
        unmarked_numbers = [x for x in self.used_numbers if x not in self.marked_numbers]
        return sum(unmarked_numbers) * self.marked_numbers[-1]


def data_refinement(raw_input_data) -> Tuple[List[int], List[BingoBoard]]:
    """Do some refinement on the input data"""
    # first line is the line of drawn numbers
    numbers_to_draw = [int(x.rstrip()) for x in raw_input_data[0].split(',')]
    boards: List[BingoBoard] = []
    board_iter = iter(raw_input_data[1:])
    done_looping = False

    while not done_looping:
        raw_lines = []
        try:
            # skip empty lines
            next(board_iter)
            for _ in range(5):
                raw_lines.append([int(x.rstrip()) for x in next(board_iter).split(' ') if x != ''])
            boards.append(BingoBoard(raw_lines))
        except StopIteration:
            done_looping = True

    return numbers_to_draw, boards


def part_one(input_data: Tuple[List[int], List[BingoBoard]]) -> int:
    """Part one"""
    we_have_a_winner = False
    wining_board = 1
    for drawn_number in input_data[0]:
        for board in input_data[1]:
            board.check_for_hit(drawn_number)
            if board.check_for_win():
                we_have_a_winner = True
                winning_board = board
                break
        if we_have_a_winner:
            break
    if not we_have_a_winner:
        print("didn't found any winning board")
    return winning_board.calc_wining_score()


def part_two(input_data: Tuple[List[int], List[BingoBoard]]) -> int:
    """Part Two"""
    all_boards = len(input_data[1])
    number_iter = iter(input_data[0])
    not_done = True
    while not_done:
        drawn_number = next(number_iter)
        for board in input_data[1]:
            board.check_for_hit(drawn_number)
            board.check_for_win()
        all_won_boards_so_far = len([1 for b in input_data[1] if b.has_won])
        if all_won_boards_so_far == all_boards - 1:
            [loosing_board] = [b for b in input_data[1] if not b.has_won]
            not_done = False

    while not loosing_board.has_won:
        loosing_board.check_for_hit(next(number_iter))
        loosing_board.check_for_win()

    return loosing_board.calc_wining_score()


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
