"""
Tests for calculation of largest prime factor.
"""

import unittest
from largest_prime_factor import largest_prime_factor


class TestLargestPrimeFactor(unittest.TestCase):
    """
    Test for largest prime factor.
    """

    def test_13195_29(self):
        """
        Test that largest prime factor of 13195 is 29.
        """
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_600851475143_6857(self):
        """
        Test that largest prime factor of 600851475143 is 6857.
        """
        self.assertEqual(largest_prime_factor(600851475143), 6857)


if __name__ == "__main__":
    unittest.main()
