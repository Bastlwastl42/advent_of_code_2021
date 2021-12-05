from math import sqrt
from pathlib import Path
from typing import Tuple, List

from utils.file import readin_files


class MyVector:
    """Yet another 2dim-vector class, because Math is fun."""

    def __init__(self, input_tuple: Tuple):
        self.x = float(input_tuple[0])
        self.y = float(input_tuple[1])

    def vector_length(self):
        """return the norm of a 2-dim vector"""
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        """vectors are equals if their components are equal"""
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __add__(self, other):
        """Add the components to have yet antoher vector"""
        return MyVector((self.x + other.x, self.y + other.y))

    def skalar_mult(self, skalar):
        """expand a vector by multiplying all components with a skalar value"""
        return MyVector((self.x * skalar, self.y * skalar))

    def normalize(self):
        """this only works because we deal with simple cases.
        If you know LinAlg, please look away."""
        if self.x == 0:
            final_x = 0
        else:
            final_x = 1 if self.x > 0 else -1
        if self.y == 0:
            final_y = 0
        else:
            final_y = 1 if self.y > 0 else -1
        return MyVector((final_x, final_y))


def difference(theone: MyVector, other: MyVector) -> MyVector:
    start = other.x - theone.x
    end = other.y - theone.y
    return MyVector((start, end))


def inlinewith(theone: MyVector, other: MyVector) -> bool:
    if theone.x == other.x or theone.y == other.y:
        return True
    return False


class VentField:
    """A class to represent the search field."""

    def __init__(self, size):
        """
        init by given size, 1000 should do for the input as there were more or less 3 digit
            coordindates.
        """
        self.field = [[0 for _ in range(size)] for _ in range(size)]

    def inc_value(self, position: MyVector):
        """increase the value at a given vector/coordindate"""
        self.field[int(position.x)][int(position.y)] += 1

    def place_line(self, start: MyVector, end: MyVector):
        """increase values between start and end"""
        # get direction
        direction = difference(start, end)
        direction = direction.normalize()
        counter = 0
        reached_end = False
        while not reached_end:
            next_coordinate = start + direction.skalar_mult(counter)
            self.inc_value(next_coordinate)
            if next_coordinate == end:
                reached_end = True
            counter += 1

    def __repr__(self):
        """i thought this helps printing"""
        [print(row) for row in self.field]

    def __str__(self):
        """this might help printing"""
        return [f"{row}\n" for row in self.field]

    def spot_hot_areas(self):
        """the searched value is all the hot spots where (at least) two lines cross."""
        spot_counter = 0
        for row in self.field:
            spot_counter += len([x for x in row if x > 1])
        return spot_counter


def data_refinement(raw_input_data):
    """Do some refinement on the input data"""
    ret_list = []
    for line in raw_input_data:
        split_lines = line.split(' -> ')
        ret_list.append((MyVector(split_lines[0].split(',')), MyVector(split_lines[1].split(','))))

    return ret_list


def part_one(input_data: List[Tuple[MyVector, MyVector]], field_size: int = 10):
    """Part one"""
    my_field = VentField(field_size)
    # only consider horizontal/vertical lines
    for start, end in input_data:
        if not inlinewith(start, end):
            continue
        my_field.place_line(start, end)
    return my_field.spot_hot_areas()


def part_two(input_data: List[Tuple[MyVector, MyVector]], field_size: int = 10):
    """Part Two"""
    my_field = VentField(field_size)
    for start, end in input_data:
        my_field.place_line(start, end)
    return my_field.spot_hot_areas()


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    input_data = data_refinement(raw_data)

    print(part_one(input_data, 1000))
    print(part_two(input_data, 1000))
