import unittest
from pathlib import Path

from day_three.day_03 import data_refinement, part_one, part_two, binary_string_to_int
from utils.file import readin_files


class TestDay03(unittest.TestCase):

    def setUp(self):
        """load data and run refinements"""
        test_assets = Path.cwd() / 'assets'
        self.raw_input = readin_files('test_input.txt', test_assets)
        self.input_data = data_refinement(self.raw_input)

    def test_bit_string(self):
        """test the bitstring function"""
        self.assertEqual(22, binary_string_to_int('10110'))

    def test_part_one(self):
        """test part one"""
        self.assertEqual((22, 9, 198), part_one(self.input_data))

    def test_part_two(self):
        """Test part two"""
        self.assertEqual((23, 10, 230), part_two(self.input_data))
