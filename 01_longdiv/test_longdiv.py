#!/usr/bin/env python3

import unittest
from longdiv_stripped import long_division

class TestLongDivision(unittest.TestCase):

    def test_zero_dividend(self):
        result = long_division(0, 10) 
        self.assertEqual(result, "0|10\n0 |0\n")

    def test_zero_divider(self):
        with self.assertRaises(ZeroDivisionError):
            long_division(10, 0)

    def test_negative_numbers(self):
        result = long_division(-10, 2)
        self.assertEqual(result, "-10|2\n-5 |0\n")

    def test_large_numbers(self):
        dividend = 1000000000
        divider = 12345678
        result = long_division(dividend, divider) 
        # assert long result

    def test_remainder_calculation(self):
        result = long_division(25, 7)
        self.assertEqual(result, "25|7\n3 |4\n")

    def test_string_input(self):
        with self.assertRaises(TypeError):
            long_division("10", 2)

    def test_float_input(self):
        result = long_division(10.5, 2)
        self.assertEqual(result, "10|2\n5 |0\n")

if __name__ == '__main__':
    unittest.main()