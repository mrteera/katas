from mock import patch
from operator import add, mul, sub, div
import random
import unittest

class TestCaptcha(unittest.TestCase):
    def setUp(self):
        self.captcha = Captcha()

    @patch('random.randint')
    def test_random_should_be_called_in_gen_number(self, mock):
        self.captcha.gen_number()
        mock.assert_called_once_with(1, 10)

    @patch('__main__.Captcha.gen_number')
    def test_gen_number_should_return_number_1_to_10(self, mock):
        mock.return_value = 1
        result = self.captcha.gen_number()
        self.assertEqual(result, 1)

        mock.return_value = 2
        result = self.captcha.gen_number()
        self.assertEqual(result, 2)

        mock.return_value = 4
        result = self.captcha.gen_number()
        self.assertEqual(result, 4)

    @patch('random.choice')
    def test_random_should_be_called_in_gen_op(self, mock):
        self.captcha.gen_op()
        mock.assert_called_once_with((add, mul, sub, div))


class Captcha():
    def gen_number(self):
        return random.randint(1, 10)

    def gen_op(self):
        operators = (add, mul, sub, div)
        return random.choice(operators)

if __name__ == '__main__':
    unittest.main()
