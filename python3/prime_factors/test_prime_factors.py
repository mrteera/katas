import unittest

from prime_factors import PrimeFactor

class TestPrimeFactor(unittest.TestCase):

    def setUp(self):
        self.prime_factors = PrimeFactor()

    def test_1_should_return_empty_list(self):
        actual = self.prime_factors.put(1)
        expected = []
        self.assertEqual(expected, actual)

    def test_2_should_return_list_of_2(self):
        actual = self.prime_factors.put(2)
        expected = [2]
        self.assertEqual(expected, actual)

    def test_3_should_return_list_of_3(self):
        actual = self.prime_factors.put(3)
        expected = [3]
        self.assertEqual(expected, actual)

    def test_4_should_return_list_of_2_2(self):
        actual = self.prime_factors.put(4)
        expected = [2,2]
        self.assertEqual(expected, actual)

    def test_15_should_return_list_of_3_5(self):
        actual = self.prime_factors.put(15)
        expected = [3,5]
        self.assertEqual(expected, actual)
