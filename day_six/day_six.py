from copy import copy
from pathlib import Path
from typing import Dict

from utils.file import readin_files


class School:
    """Defines a school of lantern fish"""
    max_age: int = 8
    repro_reset_age: int = 6
    newborn_age: int = 8

    def __init__(self, input_data):
        """Fill in structure with histogram values from the input"""
        self.all_fish: Dict[int, int] = {x: 0 for x in range(self.max_age)}
        self.all_fish[-1] = 0
        for counter in range(self.max_age + 1):
            self.all_fish[counter] = len([x for x in input_data if x == counter])

    def live_another_day(self):
        """Swap every entry on the dict by one day (less)"""
        new_school = {}
        # reduce every entry by 1
        for counter in range(self.max_age + 1):
            new_school[counter - 1] = self.all_fish.get(counter, 0)

        # add entry for -1 to 6
        new_school[self.repro_reset_age] += new_school[-1]

        # add new fish according to mature fish
        new_school[self.newborn_age] = new_school[-1]

        self.all_fish = copy(new_school)

    def count_all_the_fish(self) -> int:
        """Yeah, count all the fish"""
        return sum([x for days, x in self.all_fish.items() if days >= 0])

    def __str__(self):
        return f"{';  '.join([f'{x}: {y}' for x, y in self.all_fish.items()])}"


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
    myschool = School(input_data)
    for counter in range(days):
        myschool.live_another_day()
        # print(myschool)

    return myschool.count_all_the_fish()


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data, 80))
    print(part_two(input_data, 256))
