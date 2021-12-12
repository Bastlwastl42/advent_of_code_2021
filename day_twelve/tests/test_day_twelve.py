import unittest
from pathlib import Path

from day_twelve.day_twelve import data_refinement, part_one, part_two
from utils.file import readin_files


class TestDay12(unittest.TestCase):

    def setUp(self):
        """load data and run refinements"""
        test_assets = Path.cwd() / 'assets'
        self.input_data = []
        for counter in range(3):
            self.raw_input = readin_files(f'test_input_{counter + 1}.txt', test_assets)
            self.input_data.append(data_refinement(self.raw_input))

    def test_part_one(self):
        """test part one"""
        expected_paths = [10, 19, 226]
        for act_input, expectation in zip(self.input_data, expected_paths):
            with self.subTest(f"testing next input with {expectation} amount of paths"):
                self.assertEqual(expectation, part_one(act_input))

    def test_part_two(self):
        """Test part two"""
        expected_paths = [36, 103, 3509]
        for act_input, expectation in zip(self.input_data, expected_paths):
            with self.subTest(f"testing next input with {expectation} amount of paths"):
                self.assertEqual(expectation, part_two(act_input))
