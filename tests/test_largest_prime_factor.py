import unittest
from largest_prime_factor import largest_prime_factor


class TestLargestPrimeFactor(unittest.TestCase):

    def test_1(self):
        self.assertEqual(largest_prime_factor(1), 1)

    def test_2(self):
        self.assertEqual(largest_prime_factor(2), 2)

    def test_3(self):
        self.assertEqual(largest_prime_factor(3), 3)

    def test_4(self):
        self.assertEqual(largest_prime_factor(4), 2)

    def test_prime(self):
        self.assertEqual(largest_prime_factor(5), 5)
        self.assertEqual(largest_prime_factor(7), 7)

    def test_power_2(self):
        self.assertEqual(largest_prime_factor(8), 2)
        self.assertEqual(largest_prime_factor(16), 2)

    def test_prime_factors(self):
        self.assertEqual(largest_prime_factor(35), 7)
        self.assertEqual(largest_prime_factor(385), 11)

    def test_square_prime(self):
        self.assertEqual(largest_prime_factor(25), 5)
        self.assertEqual(largest_prime_factor(49), 7)

    def test_square_even(self):
        self.assertEqual(largest_prime_factor(36), 3)
        self.assertEqual(largest_prime_factor(100), 5)

    def test_square_odd(self):
        self.assertEqual(largest_prime_factor(81), 3)
        self.assertEqual(largest_prime_factor(225), 5)

    def test_general(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(600851475143), 6857)


if __name__ == "__main__":
    unittest.main()
