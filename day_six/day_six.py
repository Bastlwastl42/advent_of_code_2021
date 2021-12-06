from pathlib import Path

from utils.file import readin_files


def data_refinement(raw_input_data):
    """Do some refinement on the input data"""
    return [int(x.rstrip()) for x in raw_input_data[0].split(',')]


def part_one(school, days):
    """Part one"""
    print(f'Initial State: {",".join([str(fish) for fish in school])}')
    for counter in range(days):
        # decrease every entry of the swarm
        school = [fish - 1 for fish in school]
        # replace every -1 with a six and append a new fish with 8
        for index in [i for i, fish in enumerate(school) if fish == -1]:
            school[index] = 6
            school.append(8)
        if counter % 25 == 0:
            # print(f'After\t {counter} days: \t {",".join([str(fish) for fish in school])}')
            print(f'After\t {counter} days: \t {len(school)}')
    return len(school)


def part_two(input_data, days):
    """Part Two"""
    part_one(input_data, days)


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data, 80))
    print(part_two(input_data, 256))
