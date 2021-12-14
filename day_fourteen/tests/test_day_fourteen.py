import unittest
from pathlib import Path

from day_fourteen.day_fourteen import data_refinement, part_one, part_two
from utils.file import readin_files


class TestDay14(unittest.TestCase):

    def setUp(self):
        """load data and run refinements"""
        test_assets = Path.cwd() / 'assets'
        self.raw_input = readin_files('test_input.txt', test_assets)
        self.input_start, self.input_inserts = data_refinement(self.raw_input)

    def test_part_one(self):
        """test part one"""
        self.assertEqual(1588, part_one(self.input_start, self.input_inserts, 10))

    def test_part_two(self):
        """Test part two"""
        self.assertEqual(2188189693529, part_two(self.input_start, self.input_inserts, 40))
