import math
from pathlib import Path
from typing import List, Dict

from utils.file import readin_files

OPEN_CHARS: List[str] = ['(', '[', '<', '{']
CLOSE_CHARS: List[str] = [')', ']', '>', '}']
POINTS_INCORRECT: Dict[str, int] = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
POINTS_INCOMPLETE: Dict[str, int] = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
CHAR_MATCH: Dict[str, str] = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>',
}


def data_refinement(raw_input_data):
    """Do some refinement on the input data"""
    return [x.rstrip() for x in raw_input_data]


def parse_through_line(line_iter, opener_list: List[str]) -> (int, List[str]):
    for next_char in line_iter:
        if next_char in OPEN_CHARS:
            # go one level deeper
            opener_list.append(next_char)
            act_score, opener_list = parse_through_line(line_iter, opener_list)
            if act_score != 0:
                return act_score, opener_list
            continue
        if next_char in CLOSE_CHARS:
            # closing char must match
            if CHAR_MATCH[opener_list[-1]] != next_char:
                return POINTS_INCORRECT[next_char], opener_list
            opener_list.pop()
    return 0, opener_list


def part_one(input_data) -> int:
    """Part one"""
    ret_score = 0
    for line in input_data:
        ret_score += parse_through_line(iter(line[1:]), [line[0]])[0]

    return ret_score


def part_two(input_data):
    """Part Two"""
    all_scores: List[int] = []
    for line in input_data:
        # check line for correctness
        line_score, my_opener_list = parse_through_line(iter(line[1:]), [line[0]])
        if line_score != 0:
            # discard invalid lines
            continue
        # the line is incomplete, so expand and try again
        act_score = 0
        for char in reversed(my_opener_list):
            act_score *= 5
            act_score += POINTS_INCOMPLETE[CHAR_MATCH[char]]
        all_scores.append(act_score)
    all_scores.sort()
    # find middle
    mid = math.floor(len(all_scores)*0.5)
    return all_scores[mid]


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
