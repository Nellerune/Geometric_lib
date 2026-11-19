import unittest
import square

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

    def test_perimeter_fraction(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10)
