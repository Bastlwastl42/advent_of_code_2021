from pathlib import Path
from typing import Tuple, List, Dict

from utils.file import readin_files

POSS_ADJ = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]


class Octopuss:

    def __init__(self, pos: Tuple[int, int], value: int):
        """construct an Octopuss by inistial value and position"""
        self.value = value
        self.pos = pos
        self.flashed_this_round = False
        self.neighbors: List[Tuple[int, int]] = []
        for adj in POSS_ADJ:
            next_pos = (pos[0] + adj[0], pos[1] + adj[1])
            if next_pos[0] == -1 or next_pos[1] == -1:
                continue
            self.neighbors.append(next_pos)

    def regular_increase(self):
        """Include here the reset of the flashed value
        only called at the beginning"""
        self.flashed_this_round = False
        self.value += 1

    def flash_increase(self):
        self.value += 1

    def regular_end(self):
        if self.flashed_this_round:
            self.value = 0

    def check_for_flash(self) -> bool:
        """
        if self.value is larger than 9
        """
        return self.value > 9

    def do_flash(self):
        """
        set flashed this round of and increase value for neighboars
        """
        self.flashed_this_round = True


def data_refinement(raw_input_data) -> Dict[Tuple[int, int], Octopuss]:
    """Do some refinement on the input data"""
    return {(row, col): Octopuss(value=int(x.rstrip()), pos=(row, col))
            for col, line in enumerate(raw_input_data) for row, x in enumerate(line) if
            x.rstrip() != ''}


def update_octopussies(input_data: Dict[Tuple[int, int], Octopuss]):
    # increase every octpuss
    [o.regular_increase() for o in input_data.values()]
    new_adds: List[Octopuss] = [o for o in input_data.values() if o.check_for_flash()]
    while len(new_adds) > 0:
        for o in new_adds:
            o.do_flash()
            [input_data.get(pos, Octopuss((-1, -1), 1)).flash_increase() for pos in
             o.neighbors]
        new_adds = [o for o in input_data.values() if
                    o.check_for_flash() and not o.flashed_this_round]
    [o.regular_end() for o in input_data.values()]
    return len([o for o in input_data.values() if o.flashed_this_round])


def part_one(input_data: Dict[Tuple[int, int], Octopuss], rounds) -> int:
    """Part one"""
    flash_counter = 0
    for _ in range(rounds):
        flash_counter += update_octopussies(input_data)
    return flash_counter


def part_two(input_data: Dict[Tuple[int, int], Octopuss]):
    """Part Two"""
    round_counter = 0
    all_octi = len(input_data)
    flashed_this_round = 0
    while not flashed_this_round == all_octi:
        flashed_this_round = update_octopussies(input_data)
        round_counter += 1
    return round_counter


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data, 100))
    print(part_two(input_data))
