from pathlib import Path

from utils.file import readin_files


def day_two_part_one(input_data):
    depth_counter = 0
    forward_counter = 0
    for direction, length in input_data:
        if direction == 'forward':
            forward_counter += int(length)
        elif direction == 'down':
            depth_counter += int(length)
        elif direction == 'up':
            depth_counter -= int(length)
    return forward_counter, depth_counter, forward_counter * depth_counter


def day_two_part_two(input_data):
    forward_counter = 0
    aim_counter = 0
    depth_counter = 0
    for direction, length in input_data:
        if direction == 'forward':
            forward_counter += int(length)
            depth_counter += (aim_counter * int(length))
        elif direction == 'down':
            aim_counter += int(length)
        elif direction == 'up':
            aim_counter -= int(length)

    return forward_counter, depth_counter, forward_counter * depth_counter


if __name__ == "__main__":
    input_file = 'wire_input.txt'
    input_path = Path.cwd() / 'assets'
    input_data = [line.split(' ') for line in readin_files(input_file, input_path)]
    print(day_two_part_one(input_data))
    print(day_two_part_two(input_data))
