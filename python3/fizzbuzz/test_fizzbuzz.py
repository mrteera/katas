import unittest

from fizzbuzz import FizzBuzz

class testFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_one_should_return_one(self):
        self.fizzbuzz.set_num(1)
        expected = '1'
        actual = self.fizzbuzz.get()
        self.assertEqual(expected, actual)

    def test_two_should_return_two(self):
        self.fizzbuzz.set_num(2)
        expected = '2'
        actual = self.fizzbuzz.get()
        self.assertEqual(expected, actual)

    def test_three_should_return_fizz(self):
        self.fizzbuzz.set_num(3)
        expected = 'fizz'
        actual = self.fizzbuzz.get()
        self.assertEqual(expected, actual)

    def test_five_should_return_buzz(self):
        self.fizzbuzz.set_num(5)
        expected = 'buzz'
        actual = self.fizzbuzz.get()
        self.assertEqual(expected, actual)

    def test_fifteen_should_return_fizzbuzz(self):
        self.fizzbuzz.set_num(15)
        expected = 'fizzbuzz'
        actual = self.fizzbuzz.get()
        self.assertEqual(expected, actual)
