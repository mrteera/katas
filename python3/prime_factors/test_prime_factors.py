import unittest

from prime_factors import PrimeFactors

class TestPrimeFactors(unittest.TestCase):

    def setUp(self):
        self.prime_factors = PrimeFactors()

    def test_1_should_return_empty_list(self):
        expected = []
        actual = self.prime_factors.put(1)
        self.assertEqual(expected, actual)

    def test_2_should_return_list_of_2(self):
        expected = [2]
        actual = self.prime_factors.put(2)
        self.assertEqual(expected, actual)
