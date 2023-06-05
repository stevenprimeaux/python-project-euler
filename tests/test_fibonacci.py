"""
Tests for calculations on Fibonacci sequence.
"""

import unittest
from fibonacci import (
    fibonacci_nth,
    fibonacci_nth_even,
    fibonacci_sum_upto_even
)


class TestFibonacciNthTerm(unittest.TestCase):
    """
    Test for nth term.
    """

    def test_10_55(self):
        """
        Test that 10th term is 55.
        """
        self.assertEqual(fibonacci_nth(10), 55)


class TestFibonacciNthTermEven(unittest.TestCase):
    """
    Test for nth even term.
    """

    def test_even_3_34(self):
        """
        Test that 3rd even term is 34.
        """
        self.assertEqual(fibonacci_nth_even(3), 34)


class TestFibonacciSumUptoEven(unittest.TestCase):
    """
    Test for largest even term not to exceed a certain value.
    """

    def test_upto_even_4000000_4613732(self):
        """
        Test that largest even term not to exceed 4000000 is 4613732.
        """
        self.assertEqual(fibonacci_sum_upto_even(4000000), 4613732)


if __name__ == "__main__":
    unittest.main()
