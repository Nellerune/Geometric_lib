import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_square_mul(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)
