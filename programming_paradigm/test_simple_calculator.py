import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0,0), 0)

    def setUp(self):
        self.calc = SimpleCalculator()
        
        """Test the subtraction method"""
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def setUp(self):
        self.calc = SimpleCalculator()

        """Test the multiplication method"""
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(1, -1), -1)
        self.assertEqual(self.calc.multiply(0, -3), 0)

        """Test the division  method"""
    def test_division(self):
        self.assertEqual(self.calc.divide(-1, -1), 1)
        self.assertEqual(self.calc.divide(1, -1), -1)
        self.assertEqual(self.calc.divide(2, 1), 2)
        self.assertRaises(ZeroDivisionError, self.test_divide, "error!")





        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.