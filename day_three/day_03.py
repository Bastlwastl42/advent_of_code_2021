from pathlib import Path

from utils.file import readin_files


def binary_string_to_int(bit_string):
    return sum(
        [int(x) * 2 ** y for (x, y) in zip(bit_string, range(len(bit_string)).__reversed__())])


def data_refinement(raw_input_data):
    """Do some refinement on the wire_input data"""
    return [x.rstrip() for x in raw_input_data]


def find_most_common(input_data):
    """in case of tie, return 1."""
    if int(sum(input_data)) == 0.5 * len(input_data):
        return 1
    return int(sum(input_data) > 0.5 * len(input_data))


def part_one(input_data):
    """Part one"""
    epsilon = []
    gamma = []
    bit_length = len(input_data[0])
    for counter in range(bit_length):
        all_gamma_bits_pos = [int(x[counter]) for x in input_data]
        if sum(all_gamma_bits_pos) > 0.5 * len(input_data):
            epsilon.extend('0')
            gamma.extend('1')
        else:
            epsilon.extend('1')
            gamma.extend('0')

    ret_gamma = binary_string_to_int(gamma)
    ret_epsilon = binary_string_to_int(epsilon)
    return ret_gamma, ret_epsilon, ret_epsilon * ret_gamma


def part_two(input_data):
    """Part Two"""
    remainder = input_data
    for counter in range(len(input_data[0])):
        most_common = find_most_common([int(x[counter]) for x in remainder])
        remainder = [x for x in remainder if int(x[counter]) == most_common]
        if len(remainder) <= 1:
            break

    [oxygen] = remainder
    print(f"oxygen/most common{binary_string_to_int(oxygen.rstrip())}")
    ret_oxy = binary_string_to_int(oxygen)
    remainder = input_data
    for counter in range(len(input_data[0])):
        least_common = int(not bool(find_most_common([int(x[counter]) for x in remainder])))
        remainder = [x for x in remainder if int(x[counter]) == least_common]
        if len(remainder) <= 1:
            break

    [cotwo] = remainder
    print(f"co2/least common {binary_string_to_int(cotwo)}")
    retcotwo = binary_string_to_int(cotwo)

    return ret_oxy, retcotwo, retcotwo * ret_oxy


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'wire_input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data))
    print(part_two(input_data))
