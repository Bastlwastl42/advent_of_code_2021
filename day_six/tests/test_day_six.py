import unittest
from pathlib import Path

from day_six.day_six import data_refinement, part_one, part_two
from utils.file import readin_files


class TestDay06(unittest.TestCase):

    def setUp(self):
        """load data and run refinements"""
        test_assets = Path.cwd() / 'assets'
        self.raw_input = readin_files('test_input.txt', test_assets)
        self.input_data = data_refinement(self.raw_input)

    def test_part_one(self):
        """test part one. This is the brute force and slow one"""
        assert_this = [(26, 18), (5934, 80)]

        for assert_that in assert_this:
            with self.subTest(f"Checking that {assert_that[0]} is returned after "
                              f"{assert_that[1]} days."):
                self.assertEqual(assert_that[0], part_one(self.input_data, assert_that[1]))

    def test_part_two(self):
        """Test part two, the smart one"""
        assert_this = [(26, 18), (5934, 80), (26984457539, 256)]

        for assert_that in assert_this:
            with self.subTest(f"Checking that {assert_that[0]} is returned after "
                              f"{assert_that[1]} days."):
                self.assertEqual(assert_that[0], part_two(self.input_data, assert_that[1]))
