from pathlib import Path
from typing import Dict

from utils.file import readin_files


def data_refinement(raw_input_data):
    """Do some refinement on the wire_input data"""
    return [int(x.rstrip()) for x in raw_input_data[0].split(',')]


def dergutealtegauss(steps: int) -> int:
    return int((steps * (steps + 1)) * 0.5)


def part_one(input_data):
    """Part one"""
    min_pos = min(input_data)
    max_pos = max(input_data)
    all_fuel_costs: Dict = {}
    for test_mid in [x for x in range(max_pos + 1) if x >= min_pos]:
        all_fuel_costs[test_mid] = (sum([abs(crap_pos - test_mid) for crap_pos in input_data]))

    min_fuel = min(all_fuel_costs.values())
    [min_fuel_index] = [key for key, val in all_fuel_costs.items() if val == min_fuel]
    return min_fuel_index, min_fuel


def part_two(input_data):
    """Part Two"""
    min_pos = min(input_data)
    max_pos = max(input_data)
    all_fuel_costs: Dict = {}
    for test_mid in [x for x in range(max_pos + 1) if x >= min_pos]:
        all_fuel_costs[test_mid] = (
            sum([dergutealtegauss(abs(crap_pos - test_mid)) for crap_pos in input_data]))

    min_fuel = min(all_fuel_costs.values())
    [min_fuel_index] = [key for key, val in all_fuel_costs.items() if val == min_fuel]
    return min_fuel_index, min_fuel


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'wire_input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
