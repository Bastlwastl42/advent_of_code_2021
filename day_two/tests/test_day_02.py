import unittest
from day_two.day_02 import day_two_part_two, day_two_part_one
from pathlib import Path
from utils.file import readin_files


class TestDayTwo(unittest.TestCase):
    """Testing for day two"""

    def setUp(self):
        """"""
        self.input_file = 'test_input.txt'
        self.input_path = Path.cwd() / 'assets'
        self.input_data = [lin.split(' ') for lin in readin_files(self.input_file, self.input_path)]

    def test_day_two_part_one(self):
        """testing part one"""
        self.assertEqual((15, 10, 150), day_two_part_one(self.input_data))

    def test_day_two_part_two(self):
        """testing part two"""
        self.assertEqual((15, 60, 900), day_two_part_two(self.input_data))

if __name__ == "__main__":
    unittest.main()
