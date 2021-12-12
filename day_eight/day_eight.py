from pathlib import Path
from typing import List

from utils.file import readin_files


class Display:

    def __init__(self, wire_input):
        """Store sorted display wires"""
        self.wires = sorted(wire_input)
        # these input don't appear to be random, for larger values they might be
        if len(self.wires) == 2:
            self.number = 1
            self.actual_seg = ['c', 'f']
        elif len(self.wires) == 3:
            self.number = 7
            self.actual_seg = ['a', 'c', 'f']
        elif len(self.wires) == 4:
            self.number = 4
            self.actual_seg = ['b', 'c', 'e', 'f']
        elif len(self.wires) == 7:
            self.number = 8
        else:
            self.number = -1

    def set_number(self, number):
        self.number = number

    def __eq__(self, other):
        if len(self.wires) != len(other.wires):
            return False
        return all([x == y for x, y in zip(self.wires, other.wires)])


def data_refinement(raw_input_data):
    """Do some refinement on the wire_input data"""
    ret_obs = []
    ret_disp = []
    for line in raw_input_data:
        observations, display = line.split('|')
        ret_obs.append([Display(x) for x in observations.split(' ') if x != ''])
        ret_disp.append([Display(x.rstrip()) for x in display.split(' ') if x != ''])

    return ret_obs, ret_disp


def part_one(observations: List[Display], displays: List[Display]):
    """Part one"""
    easy_values = [1, 4, 7, 8]
    display_counter = 0
    for disp in displays:
        display_counter += sum([1 for d in disp if d.number in easy_values])

    return display_counter


def part_two(observations: List[Display], displays: List[Display]):
    """Part Two"""
    decoded_display = []
    for obs, disp in zip(observations, displays):
        seg_dict = {}
        # determine the a element from being in 7 but not in 1
        [seven] = [x for x in obs if x.number == 7]
        [one] = [x for x in obs if x.number == 1]
        seg_dict['a'] = [x for x in seven.wires if x not in one.wires][0]

        # determine d from common element in 2, 3, 4, 5
        [four] = [x for x in obs if x.number == 4]
        fivers = [x for x in obs if len(x.wires) == 5]
        fivers.append(four)
        remainers = list({y for x in fivers for y in x.wires})
        for d in fivers:
            remainers = [x for x in d.wires if x in remainers]
        seg_dict['d'] = remainers[0]

        # zero is the six-digit diaplys with no d element
        [zero] = [x for x in obs if len(x.wires) == 6 and seg_dict['d'] not in x.wires]
        zero.set_number(0)

        # five is in 6 and 9
        sixers = [x for x in obs if len(x.wires) == 6 and x.number == -1]
        for f in fivers:
            overlap = 0
            for s in sixers:
                overlap += len([x for x in f.wires if x in s.wires])
            if overlap == 10:
                five = f
                five.set_number(5)
                break

        # three has one completely in it
        fivers = [x for x in obs if len(x.wires) == 5 and x.number == -1]
        for f in fivers:
            overlap = [x for x in f.wires if x in one.wires]
            if len(overlap) == 2:
                three = f
                three.set_number(3)
                [two] = [x for x in fivers if x.number == -1]
                two.set_number(2)
                break

        # three is completely in 9
        for s in sixers:
            overlap = [x for x in s.wires if x in three.wires]
            if len(overlap) == 5:
                nine = s
                nine.set_number(9)
                [six] = [x for x in sixers if x.number == -1]
                six.set_number(6)

        for d in disp:
            if d.number != -1:
                continue
            [ident] = [x for x in obs if x == d]
            d.set_number(ident.number)
        if [x for x in obs if x.number == -1]:
            print('panic')
        dec_disp = int(''.join([str(x.number) for x in disp]))
        decoded_display.append(dec_disp)

    return sum(decoded_display)


if __name__ == "__main__":
    """Load data and send to functions"""
    input_file = 'input.txt'
    input_path = Path.cwd() / 'assets'
    raw_data = readin_files(input_file, input_path)
    observations, displays = data_refinement(raw_data)

    print(part_one(observations, displays))
    print(part_two(observations, displays))
