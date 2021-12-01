from pathlib import Path
from typing import List

from utils.file import readin_files


def convert_to_num(line: str):
    """strip away newline and convert"""
    return int(line.rstrip())


def gimme_three(numbers: List, start: int = 0):
    """return the next 3 elements starting the given"""
    return [numbers[start], numbers[start + 1], numbers[start + 2]]


def day_one_part_one(input_file: str, input_path: Path):
    """solving puzzle one for day one: doing integrations"""

    file_content = readin_files(input_file, input_path)
    prev = None
    increase_counter = 0
    decrease_counter = 0
    for line in file_content:
        if prev:
            act_val = convert_to_num(line)
            if act_val > prev:
                increase_counter = increase_counter + 1
            elif act_val < prev:
                decrease_counter = decrease_counter + 1
            elif act_val == prev:
                print('equals!')

        prev = convert_to_num(line)

    print(increase_counter)
    return increase_counter, decrease_counter


def day_one_part_two(input_file: str = 'input.txt', input_path: Path = Path.cwd()):
    """doing sliding window differentiation"""

    numbers = [convert_to_num(line) for line in readin_files(input_file, input_path)]

    increase_counter = 0
    prev = None
    for counter in range(len(numbers)-2):
        if prev:
            act = sum(gimme_three(numbers, counter))
            if act > prev:
                increase_counter = increase_counter+1

        prev = sum(gimme_three(numbers, counter))

    print(increase_counter)
    return increase_counter


if __name__ == "__main__":
    my_input_path = Path.cwd() / 'assets'
    day_one_part_one('input.txt', my_input_path)
    day_one_part_two('input.txt', my_input_path)
