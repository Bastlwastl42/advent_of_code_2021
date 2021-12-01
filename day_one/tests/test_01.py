import unittest
from day_one.day_01 import day_one_part_one, day_one_part_two
from pathlib import Path

class TestDayOne(unittest.TestCase):
    """Testing from given input"""
    def setUp(self) -> None:
        self.test_input_folder = Path.cwd() / 'assets'
        self.test_input_file = 'test_input.txt'

    def test_day_one_part_one(self):
        inc, _ = day_one_part_one(self.test_input_file, self.test_input_folder)
        self.assertEqual(7, inc)

    def test_day_one_part_two(self):
        inc = day_one_part_two(self.test_input_file, self.test_input_folder)
        self.assertEqual(5, inc)
