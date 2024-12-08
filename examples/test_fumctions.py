import unittest

from functions import (add, subtract, multiply, power, division, quotient, remain, fibonacci, leap_year)

class TestFunctions(unittest.TestCase):
    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(4, 2), 6)
        self.assertEqual(add(-5, 5), 0)
    
    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(6, 2), 4)
        self.assertEqual(subtract(6, 9), -3)
        self.assertEqual(subtract(8, 8), 0)
    
    def tes_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(6, 6), 36)
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(1, 8), 8)
    
    def test_power(self):
        """Test the power function."""
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(4, 3), 64)
        self.assertEqual(power(6, 2), 36)
    
    def tes_division(self):
        """Test the division function."""
        self.assertEqual(division(4, 2), 2.0)
        self.assertEqual(division(12, 4), 3.0)
        with self.assertRaises(ValueError):
            division(7, 0)
    
    def test_quotient(self):
        """Test the quotient function."""
        self.assertEqual(quotient(15, 5), 3)
        self.assertEqual(quotient(16, 4), 4)
        self.assertEqual(quotient(18, 3), 6)
        with self.assertRaises(ValueError):
            quotient(5, 0)
    
    def test_remain(self):
        """Test the remain function."""
        self.assertEqual(remain(10, 3), 1)
        self.assertEqual(remain(12, 4), 0)
        self.assertEqual(remain(16, 5), 1)
        with self.assertRaises(ValueError):
            remain(8, 0)
    
    def test_fibonacci(self):
        """Test the fibonacci function."""
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(2), [0, 1])
    
    def test_leap_year(self):
        """Test the leap_year function."""
        self.assertEqual(leap_year(2000), True)
        self.assertEqual(leap_year(2020), True)
        self.assertEqual(leap_year(1994), False)