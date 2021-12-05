from pathlib import Path

from utils.file import readin_files


def data_refinement(raw_input_data):
    """Do some refinement on the input data"""
    return None


def part_one(input_data):
    """Part one"""
    pass


def part_two(input_data):
    """Part Two"""
    pass


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
