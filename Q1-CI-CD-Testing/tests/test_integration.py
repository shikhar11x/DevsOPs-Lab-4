import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

from calculator_service import CalculatorService


class TestCalculatorIntegration(unittest.TestCase):

    def setUp(self):
        self.service = CalculatorService()

    def test_add_operation(self):
        self.assertEqual(self.service.calculate("add", 10, 5), 15)

    def test_multiply_operation(self):
        self.assertEqual(self.service.calculate("multiply", 4, 5), 20)

    def test_divide_operation(self):
        self.assertEqual(self.service.calculate("divide", 20, 4), 5)

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            self.service.calculate("mod", 10, 3)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.service.calculate("divide", 10, 0)


if __name__ == "__main__":
    unittest.main()
