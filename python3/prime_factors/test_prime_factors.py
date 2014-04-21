import unittest

from prime_factors import PrimeFactor

class TestPrimeFactor(unittest.TestCase):

    def test_1_should_return_empty_list(self):
        self.prime_factors = PrimeFactor()
        actual = self.prime_factors.put(1)
        expected = []
        self.assertEqual(expected, actual)

    def test_2_should_return_list_of_2(self):
        self.prime_factors = PrimeFactor()
        actual = self.prime_factors.put(2)
        expected = [2]
        self.assertEqual(expected, actual)

    def test_3_should_return_list_of_3(self):
        self.prime_factors = PrimeFactor()
        actual = self.prime_factors.put(3)
        expected = [3]
        self.assertEqual(expected, actual)

    def test_4_should_return_list_of_2_2(self):
        self.prime_factors = PrimeFactor()
        actual = self.prime_factors.put(4)
        expected = [2,2]
        self.assertEqual(expected, actual)
