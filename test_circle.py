import math
import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_one(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_two(self):
        self.assertAlmostEqual(circle.area(2), 4 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_delit(self):
        self.assertAlmostEqual(circle.delit(4),2)
