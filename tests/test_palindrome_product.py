"""
Tests for palindrome products.
"""

import unittest
from src.py_euler.palindrome_product import largest_palindrome_product


class TestLargestPalindromeProduct(unittest.TestCase):
    """
    Test for largest palindrome product.
    """

    def test_2_9009(self):
        """
        Test that largest palidrome from 2-digit products is 9009.
        """
        self.assertEqual(largest_palindrome_product(2), 9009)

    def test_3_906609(self):
        """
        Test that largest palidrome from 3-digit products is 906609.
        """
        self.assertEqual(largest_palindrome_product(3), 906609)


if __name__ == "__main__":
    unittest.main()
