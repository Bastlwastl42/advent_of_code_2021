import math
from pathlib import Path
from typing import List, Dict, Tuple, Union

from utils.file import readin_files


class Heatmap:
    heat: Dict[Tuple[int, int], Dict[str, Union[int, bool, None]]] = {}
    check_pattern = [(+1, 0), (-1, 0), (0, +1), (0, -1)]
    basin_dict: Dict[Tuple[int, int], List[Tuple[int, int]]] = {}

    def __init__(self, input_rows: List[List[int]]):
        """Constructor"""
        for row_counter, row in enumerate(input_rows):
            for col_counter, value in enumerate(row):
                self.heat[(row_counter, col_counter)] = {'value': value,
                                                         'is_min': None,
                                                         'risk_level': -1}

    def check_for_minimum(self):
        """
        Go through fields an check neighbors.
        """

        for coordinates, val_dict in self.heat.items():
            if type(val_dict['is_min']) == type(bool):
                continue
            # go though everything and check the surroundings
            to_check = [(coordinates[0] + pattern[0], coordinates[1] + pattern[1])
                        for pattern in self.check_pattern]
            is_min = True
            for sur_dict in [x for c, x in self.heat.items() if c in to_check]:
                is_min = val_dict['value'] < sur_dict['value']
                if not is_min:
                    break
            val_dict['is_min'] = is_min

    def calc_risk_level(self) -> int:
        """every minimum has a risk level it's hight plus one"""
        for val_dict in [x for x in self.heat.values() if x['is_min']]:
            val_dict['risk_level'] = val_dict['value'] + 1
        return sum([x['risk_level'] for x in self.heat.values() if x['is_min']])

    def do_basin_creep(self):
        """starting from every minimum, go left in all dirs until stopped by a 9"""
        for min_cor in [c for c, v in self.heat.items() if v['is_min']]:
            not_stopped = True
            act_basin = [min_cor]
            while not_stopped:
                act_length = len(act_basin)
                print(f"checking {act_length} elements")
                for act_cor in act_basin:
                    for dir in self.check_pattern:
                        counter = 1
                        while True:
                            # run in a single direction until hitting walls or a nine
                            next_cor = (
                                act_cor[0] + (dir[0] * counter), act_cor[1] + (dir[1] * counter))
                            next_val = self.heat.get(next_cor, None)
                            if not next_val:
                                break
                            if next_val['value'] == 9:
                                break
                            # add corr to list and increment
                            if next_cor not in act_basin:
                                act_basin.append(next_cor)
                            counter += 1

                not_stopped = not (act_length == len(act_basin))
            self.basin_dict[min_cor] = act_basin

    def find_top_three_basin(self):
        """
        calc value for part two
        """
        all_basins_sorted = sorted([len(b) for b in self.basin_dict.values()], reverse=True)
        print(all_basins_sorted[0:3])
        return math.prod(all_basins_sorted[0:3])


def data_refinement(raw_input_data):
    """Do some refinement on the input data"""
    ret: List[List[int]] = []
    for row in raw_input_data:
        ret.append([int(x.rstrip()) for x in row if x != '\n'])
    return Heatmap(ret)


def part_one(input_data: Heatmap):
    """Part one"""
    input_data.check_for_minimum()
    return input_data.calc_risk_level()


def part_two(input_data):
    """Part Two"""
    input_data.check_for_minimum()
    input_data.do_basin_creep()
    return input_data.find_top_three_basin()


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
