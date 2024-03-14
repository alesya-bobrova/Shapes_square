import unittest
from shape import Circle, Triangle

class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        # Проверяем, правильно ли вычисляется площадь круга
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_area(), 78.53981633974483)

    def test_triangle_area(self):
        # Проверяем, правильно ли вычисляется площадь треугольника
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.calculate_area(), 6)

    def test_is_right_triangle(self):
        # Проверяем, правильно ли определяется, является ли треугольник прямоугольным
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())
        triangle2 = Triangle(5, 6, 7)
        self.assertFalse(triangle2.is_right_triangle())

if __name__ == "__main__":
    unittest.main()

