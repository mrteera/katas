import unittest

from berlin_clock import BerlinClock

class testBerlinClock(unittest.TestCase):
    def test_000000(self):
        berlin_clock = BerlinClock()
        berlin_clock.setTime("00:00:00")
        expected = "O OOOO OOOO OOOOOOOOOOO OOOO"
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_000001(self):
        berlin_clock = BerlinClock()
        berlin_clock.setTime("00:00:01")
        expected = "Y OOOO OOOO OOOOOOOOOOO OOOO"
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)

    def test_000101(self):
        berlin_clock = BerlinClock()
        berlin_clock.setTime("00:01:01")
        expected = "Y OOOO OOOO OOOOOOOOOOO YOOO"
        actual = berlin_clock.display()
        self.assertEqual(expected, actual)
