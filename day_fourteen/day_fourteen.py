from pathlib import Path
from typing import List, Dict, Optional

from utils.file import readin_files


class Insertion:
    """store details of a valid insertion"""

    def __init__(self, first, second, insert=None):
        self.first = first
        self.second = second
        self.insert = insert

    def __eq__(self, other) -> bool:
        """see if an insertion fits"""
        return self.first == other.first and self.second == other.second


class MyLinkedKeys:

    def __init__(self, key_value: float, next_value = None):
        self.key_value: float = key_value
        self.next_value: Optional[MyLinkedKeys] = next_value


def data_refinement(raw_input_data):
    """Do some refinement on the input data"""
    # first line is the start string
    start_dict = {MyLinkedKeys(key_value=counter): char for counter, char in
                  zip(range(len(raw_input_data)), raw_input_data[0]) if char != '\n'}
    all_inserts: List[Insertion] = []
    for line in raw_input_data[1:]:
        if line == '\n':
            continue
        line_split = line.split('->')
        all_inserts.append(Insertion(line_split[0][0], line_split[0][1], line_split[1].rstrip()))
    return start_dict, all_inserts


def get_sorted_keys(start_key: MyLinkedKeys):
    next_key = start_key
    ret = [start_key.key_value]
    while next_key:
        next_key = next_key.next_value
        if next_key:
            ret.append(next_key.key_value)
    return ret


def run_inserts(start_dict, all_inserts, rounds):
    for k in start_dict.keys():
        next_key = [nk for nk in start_dict.keys() if nk.key_value == k.key_value + 1]
        if not next_key:
            continue
        k.next_value = next_key[0]
    [start_key] = [k for k in start_dict.keys() if k.key_value == 0]
    for counter in range(rounds):
        print(f"Starting round {counter}, dict has {len(start_dict)} values.")
        current_keys = get_sorted_keys(start_key)
        for key, value in [(k, v) for k, v in start_dict.items() if k.key_value in current_keys]:
            try:
                next_key = key.next_value
            except IndexError:
                print('hit last key, finishing...')
                continue
            next_val = start_dict.get(next_key, None)
            if not next_val:
                continue
            test_insertion = Insertion(value, next_val)
            valid_insert = [i.insert for i in all_inserts if i == test_insertion]
            if valid_insert:
                new_next_key = MyLinkedKeys(key_value=(key.key_value + next_key.key_value) / 2, next_value=next_key)
                start_dict[new_next_key] = valid_insert[0].strip()
                key.next_value = new_next_key
    return start_dict


def part_one(start_dict, all_inserts, rounds):
    """Part one"""
    final_dict = run_inserts(start_dict, all_inserts, rounds)
    # find most and lest common value in dict
    unique_values: List[str] = list(set(final_dict.values()))
    results: Dict[int, str] = {}
    for char in unique_values:
        results[len([x for x in final_dict.values() if x == char])] = char
    return max(results.keys()) - min(results.keys())


def part_two(start_dict, all_inserts, rounds):
    """Part Two"""
    return part_one(start_dict, all_inserts, rounds)


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_dict, insertions = data_refinement(raw_data)

    print(part_one(input_dict, insertions, 40))
    # print(part_two(input_dict, insertions, 40))
