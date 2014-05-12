import unittest

from prime_factors import PrimeFactors

class TestPrimeFactors(unittest.TestCase):

    def test_1_should_return_empty_list(self):
        self.prime_factors = PrimeFactors()
        expected = []
        actual = self.prime_factors.put()
        self.assertEqual(expected, actual)
