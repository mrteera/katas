from unittest import TestCase
from roman import romanNumerals

class romanNumeralsTest(TestCase):
    def test_one(self):
        roman = romanNumerals()
        input_num = 1
        result = roman.from_num(input_num)
        expect = "I"
        self.assertEqual(result, expect)

    def test_four(self):
        roman = romanNumerals()
        input_num = 4
        result = roman.from_num(input_num)
        expect = "IV"
        self.assertEqual(result, expect)

    def test_five(self):
        roman = romanNumerals()
        input_num = 5
        result = roman.from_num(input_num)
        expect = "V"
        self.assertEqual(result, expect)

    def test_ten(self):
        roman = romanNumerals()
        input_num = 10
        result = roman.from_num(input_num)
        expect = "X"
        self.assertEqual(result, expect)
