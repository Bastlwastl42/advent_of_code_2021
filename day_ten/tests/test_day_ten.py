import unittest
from pathlib import Path

from day_ten.day_ten import data_refinement, part_one, part_two
from utils.file import readin_files


class TestDay10(unittest.TestCase):

    def setUp(self):
        """load data and run refinements"""
        test_assets = Path.cwd() / 'assets'
        self.raw_input = readin_files('test_input.txt', test_assets)
        self.input_data = data_refinement(self.raw_input)

    def test_part_one(self):
        """test part one"""
        self.assertEqual(26397, part_one(self.input_data))

    def test_part_two(self):
        """Test part two"""
        self.assertEqual(288957, part_two(self.input_data))
