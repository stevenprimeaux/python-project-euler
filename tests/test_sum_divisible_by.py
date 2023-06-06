"""
Tests for sum of multiples.
"""

import unittest
from src.py_euler.sum_divisible_by import sum_divisible_by_2


class TestSumDivisibleBy2(unittest.TestCase):
    """
    Tests for sum of multiples below a certain value.
    """

    def test_10_3_5(self):
        """
        Test that sum of multiples of 3 and 5 less than 10 equals 23.
        """
        self.assertEqual(sum_divisible_by_2(10, 3, 5), 23)

    def test_1000_3_5(self):
        """
        Test that sum of multiples of 3 and 5 less than 1000 equals 233168.
        """
        self.assertEqual(sum_divisible_by_2(1000, 3, 5), 233168)


if __name__ == "__main__":
    unittest.main()
