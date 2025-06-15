# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """creating an instance of SimpleCalculator before each test"""
        self.calc = SimpleCalculator()

    # addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-2, -6), -8)
        self.assertEqual(self.calc.add(-5, 5), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(3.5, 4.5), 8.0)

    # subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(15, 9), 6)
        self.assertEqual(self.calc.subtract(-2, -6), 4)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(4, 12), -8)

    # multiplication
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 6), 12)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(0, 30), 0)
        self.assertEqual(self.calc.multiply(3.5, 2), 7)

    # division
    def test_division(self):
        self.assertEqual(self.calc.divide(8, 4), 2)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(0, 7), 0)
    
    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))

        with self.assertRaises(TypeError):
            self.calc.divide("10", 2)

if __name__ == "__main__":
    unittest.main()