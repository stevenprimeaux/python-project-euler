import unittest
from largest_prime_factor import largest_prime_factor


class TestLargestPrimeFactor(unittest.TestCase):

    def test_general(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(600851475143), 6857)


if __name__ == "__main__":
    unittest.main()
