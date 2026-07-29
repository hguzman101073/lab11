# Henry and Joseph Git Code test_calculator.py
import unittest
from calculator import *
class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(3,4), 12)
        self.assertEqual(multiply(5,5), 25)
        self.assertEqual(multiply(5,0), 0)
        self.assertEqual(multiply(-2,3), -6)
        self.assertEqual(multiply(2.5,2.0), 5.0)
    def test_divide(self):
        self.assertEqual(divide(4,1), 4)
        self.assertequal(divide(12,3), 4)
        self.assertEqual(divide(-10,2), -5)
        self.assertEqual(divide(0,5), 0)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0,10)
    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3,4), 5.0)
        self.assertEqual(hypotenuse(1.5,2.0), 2.5)
        self.assertEqual(hypotenuse(0,5), 5.0)
    def test_sqrt(self):
        self.assertEqual(square_root(0), 0.0)
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(1000000), 1000.0)
        with self.assertRaise(ValueError):
            square_root(-1)

