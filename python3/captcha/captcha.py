import unittest
from mock import Mock, patch
from operator import add, sub, mul, div
import random


class test_captcah(unittest.TestCase):
    def setUp(self):
        self.captcha = Captcha()

    @patch("random.randint")
    def test_generate_first_number_should_return_1(self, mock):
        mock.return_value = 1
        result = self.captcha.gen_number()
        self.assertEqual(result, 1)

    @patch("random.randint")
    def test_generate_first_number_should_return_2(self, mock):
        mock.return_value = 2
        result = self.captcha.gen_number()
        self.assertEqual(int(result), 2)

    @patch("random.randint")
    def test_generate_last_number_should_return_1(self, mock):
        mock.return_value = 1
        result = self.captcha.gen_number()
        self.assertEqual(int(result), 1)

    @patch("random.randint")
    def test_generate_last_number_should_return_2(self, mock):
        mock.return_value = 2
        result = self.captcha.gen_number()
        self.assertEqual(int(result), 2)

    @patch("__main__.Captcha.gen_operator")
    def test_generate_operator_should_return_add(self, mock):
        mock.return_value = add
        result = self.captcha.gen_operator()
        self.assertEqual(result, add)

    @patch("__main__.Captcha.gen_number")
    def test_generate_num_in_word_return_number_in_word(self, mock):
        mock.return_value = 1
        result = self.captcha.gen_num_in_word()
        self.assertEqual(result, 'one')

        mock.return_value = 2
        result = self.captcha.gen_num_in_word()
        self.assertEqual(result, 'two')

    @patch("__main__.Captcha.gen_num_in_word")
    @patch("__main__.Captcha.gen_operator")
    @patch("__main__.Captcha.gen_number")
    def test_calculate_should_call_all_methods(
        self,
        num_mock,
        op_mock,
        word_mock
    ):
        result = self.captcha.calculate()
        num_mock.assert_called_once_with()
        op_mock.assert_called_once_with()
        word_mock.assert_called_once_with()

class Captcha():
    def calculate(self):
        pass

    def gen_num_in_word(self):
        number = self.gen_number()
        num_word_list = { 1: 'one', 2: 'two'}
        return num_word_list[number]

    def gen_number(self):
        return random.randint(1, 10)

    def gen_operator(self):
        operators = (add, sub, mul, div)
        operator = random.choice(operators)
        return operator


if __name__ == '__main__':
    unittest.main()

