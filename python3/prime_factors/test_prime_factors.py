import unittest

from prime_factors import PrimeFactors

class testPrimeFactors(unittest.TestCase):

    def setUp(self):
        self.prime_factors = PrimeFactors()

    def test_1_should_return_empty_list(self):
        self.prime_factors.set_number(1)
        actual = self.prime_factors.prime()
        expected = []
        self.assertEqual(expected, actual)

    def test_2_should_return_list_of_2(self):
        self.prime_factors.set_number(2)
        actual = self.prime_factors.prime()
        expected = [2]
        self.assertEqual(expected, actual)

    def test_3_should_return_list_of_3(self):
        self.prime_factors.set_number(3)
        actual = self.prime_factors.prime()
        expected = [3]
        self.assertEqual(expected, actual)

    def test_4_should_return_list_of_2_2(self):
        self.prime_factors.set_number(4)
        actual = self.prime_factors.prime()
        expected = [2, 2]
        self.assertEqual(expected, actual)

    def test_5_should_return_list_of_5(self):
        self.prime_factors.set_number(5)
        actual = self.prime_factors.prime()
        expected = [5]
        self.assertEqual(expected, actual)
    def test_6_should_return_list_of_2_3(self):
        self.prime_factors.set_number(6)
        actual = self.prime_factors.prime()
        expected = [2,3]
        self.assertEqual(expected, actual)
