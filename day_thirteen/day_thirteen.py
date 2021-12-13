from pathlib import Path
from typing import Dict, Tuple, List

from utils.file import readin_files


def data_refinement(raw_input_data) -> Dict[str, List]:
    """Do some refinement on the input data"""
    ret_coordinates_list: List[Tuple[int, int]] = []
    line_iter = iter(raw_input_data)
    for line in line_iter:
        if line == '\n':
            break
        line_split = line.split(',')
        ret_coordinates_list.append((int(line_split[0]), int(line_split[1].rstrip())))
    ret_fold_instructions_list: List[Tuple[str, int]] = []
    for line in line_iter:
        fold_inst = line.split(' ')[2].split('=')
        ret_fold_instructions_list.append((fold_inst[0], int(fold_inst[1].rstrip())))
    return {'coordindates': ret_coordinates_list, 'foldings': ret_fold_instructions_list}


def do_horizontal_fold(list_of_coords: List[Tuple[int, int]], mirror_value: int):
    """keep y values contant, flip all x along given valuecoordindates"""
    ret_list = []
    for point in list_of_coords:
        if point[0] < mirror_value:
            ret_list.append(point)
            continue
        ret_list.append(((2 * mirror_value) - point[0], point[1]))
    return ret_list


def do_vertical_fold(list_of_coords: List[Tuple[int, int]], mirror_value: int):
    """keep y values contant, flip all x along given valuecoordindates"""
    ret_list = []
    for point in list_of_coords:
        if point[1] < mirror_value:
            ret_list.append(point)
            continue
        ret_list.append((point[0], (2 * mirror_value) - point[1]))
    return ret_list


def do_all_folds(list_of_coordindates: List[Tuple[int, int]],
                 list_of_foldings: List[Tuple[str, int]]) -> List[Tuple[int, int]]:
    new_coors = list_of_coordindates
    for single_fold in list_of_foldings:
        if single_fold[0] == 'x':
            fold_func = do_horizontal_fold
        if single_fold[0] == 'y':
            fold_func = do_vertical_fold
        new_coors = fold_func(new_coors, single_fold[1])
    return list(set(new_coors))


def part_one(input_data: Dict[str, List]) -> int:
    """Part one"""
    # only do one fold instructions
    single_fold = input_data['foldings'][0]
    new_coors = do_all_folds(input_data['coordindates'], [single_fold])
    return len(list(set(new_coors)))


def part_two(input_data: Dict[str, List]):
    """Part Two"""
    new_coors = do_all_folds(input_data['coordindates'], input_data['foldings'])
    # a printing is in order now....
    max_x = max([x[0] for x in new_coors])+1
    max_y = max([x[1] for x in new_coors])+1
    for y in range(max_y):
        print(f"{''.join(['#' if (x, y) in new_coors else ' ' for x in range(max_x)])}")
    return 1


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
