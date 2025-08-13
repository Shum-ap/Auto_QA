import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from simple_math import SimpleMath


class TestSimpleMath(unittest.TestCase):
    """
    Юнит-тесты для класса SimpleMath.
    Проверяет корректность методов square и cube.
    """

    def setUp(self):
        """
        Выполняется перед каждым тестом.
        Создаёт экземпляр класса SimpleMath.
        """
        self.math = SimpleMath()

    # === Тесты для метода square ===

    def test_square_positive(self):
        """Проверяет возведение в квадрат положительных чисел."""
        self.assertEqual(self.math.square(2), 4)
        self.assertEqual(self.math.square(3), 9)
        self.assertEqual(self.math.square(5), 25)

    def test_square_negative(self):
        """Проверяет возведение в квадрат отрицательных чисел."""
        self.assertEqual(self.math.square(-2), 4)
        self.assertEqual(self.math.square(-3), 9)
        self.assertEqual(self.math.square(-10), 100)

    def test_square_zero(self):
        """Проверяет возведение в квадрат нуля."""
        self.assertEqual(self.math.square(0), 0)

    # === Тесты для метода cube ===

    def test_cube_positive(self):
        """Проверяет возведение в куб положительных чисел."""
        self.assertEqual(self.math.cube(2), 8)
        self.assertEqual(self.math.cube(3), 27)
        self.assertEqual(self.math.cube(4), 64)

    def test_cube_negative(self):
        """Проверяет возведение в куб отрицательных чисел."""
        self.assertEqual(self.math.cube(-2), -8)
        self.assertEqual(self.math.cube(-3), -27)
        self.assertEqual(self.math.cube(-5), -125)

    def test_cube_zero(self):
        """Проверяет возведение в куб нуля."""
        self.assertEqual(self.math.cube(0), 0)


if __name__ == '__main__':
    unittest.main()