import unittest
import triangle

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(4, 3), 6)

    def test_area_zero(self):
        self.assertEqual(triangle.area(10, 0), 0)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
