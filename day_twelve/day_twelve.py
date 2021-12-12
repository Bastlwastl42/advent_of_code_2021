import string
from pathlib import Path
from typing import List, Dict

from utils.file import readin_files


class Cave:

    def __init__(self, identifier: str, known_connections: List = []):
        """
        Construct a new cave
        big cave a given by capital case letters
        """
        self.cave_id = identifier
        self.connections: List[Cave] = []
        self.is_big_cave = self.cave_id[0] in string.ascii_uppercase
        self.is_start_cave = self.cave_id == 'start'
        for con in known_connections:
            if type(con) == type(str):
                self.connections.append(Cave(con))
            if type(con) == type(Cave):
                self.add_connection(con)

    def add_connection(self, new_connection):
        self.connections.append(new_connection)


class CavePath:

    def __init__(self, start_cave, validity_function, initial_path: List[Cave] = []):
        self.caves_in_path: List[Cave] = [start_cave]
        self.validity_function = validity_function
        if initial_path:
            self.caves_in_path.extend(initial_path)

    def is_finished(self):
        return self.caves_in_path[-1].cave_id == 'end'

    def is_valid(self) -> bool:
        """Overwrite after inheritance"""
        return self.validity_function(self)

    def expand_path(self, next_cave: Cave):
        self.caves_in_path.append(next_cave)

    def get_next_paths(self) -> List:
        """generate new paths for each possible connection of the last cave in the path"""
        if self.is_finished():
            return [self]
        ret_paths = []
        for con in self.caves_in_path[-1].connections:
            new_path = CavePath(start_cave=self.caves_in_path[0],
                                validity_function=self.validity_function,
                                initial_path=self.caves_in_path[1:])
            new_path.expand_path(con)
            ret_paths.append(new_path)
        return ret_paths


def is_valid_part_one(input_path: CavePath) -> bool:
    """small caves visited only allowed once in a Path"""
    return len([c for c in input_path.caves_in_path if not c.is_big_cave]) == \
           len(list(set([c.cave_id for c in input_path.caves_in_path if not c.is_big_cave])))


def is_valid_part_two(input_path: CavePath) -> bool:
    """a single small cave might be visited twice, bu not the start cave"""
    all_small_caves = [c.cave_id for c in input_path.caves_in_path if not c.is_big_cave]
    if len([c for c in all_small_caves if c == 'start']) > 1:
        return False
    if len([c for c in all_small_caves if c == 'end']) > 1:
        return False
    # only one cave is allowed to appear more then once
    amount_small_caves = len([c for c in input_path.caves_in_path if not c.is_big_cave])
    amount_uniqe_caves = len(
        list(set([c.cave_id for c in input_path.caves_in_path if not c.is_big_cave])))
    return amount_small_caves == amount_uniqe_caves or amount_uniqe_caves + 1 == amount_small_caves


def data_refinement(raw_input_data) -> Dict[str, Cave]:
    """Do some refinement on the input data"""
    all_caves: Dict[str, Cave] = {}
    for line in raw_input_data:
        first_cave_str, second_cave_str = line.split('-')
        second_cave_str = second_cave_str.rstrip()
        first_cave = all_caves.get(first_cave_str, Cave(first_cave_str))
        second_cave = all_caves.get(second_cave_str, Cave(second_cave_str))
        first_cave.add_connection(second_cave)
        second_cave.add_connection(first_cave)
        all_caves[first_cave_str] = first_cave
        all_caves[second_cave_str] = second_cave

    return all_caves


def run_through_paths(paths: List[CavePath]) -> List[CavePath]:
    finished_paths: List[CavePath] = []
    while paths:
        act_path = paths.pop()
        new_paths: List[CavePath] = act_path.get_next_paths()
        for np in new_paths:
            if not np.is_valid():
                continue
            if np.is_finished():
                finished_paths.append(np)
            else:
                paths.append(np)
    return finished_paths


def part_one(all_input_caves: Dict[str, Cave]):
    """Part one"""
    # get the start cave
    [start_cave] = [c for c in all_input_caves.values() if c.is_start_cave]
    return len(run_through_paths([CavePath(start_cave, is_valid_part_one)]))


def part_two(all_input_caves: Dict[str, Cave]):
    """Part Two"""
    [start_cave] = [c for c in all_input_caves.values() if c.is_start_cave]
    return len(run_through_paths([CavePath(start_cave, is_valid_part_two)]))


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
