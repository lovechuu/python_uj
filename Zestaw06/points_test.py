# Marlena Gryt
# Python 2022/2023
# Zd 6.2 

import unittest
from points import *

# Kod testujacy modul.
class TestPoint(unittest.TestCase): 

    def setUp(self):
        self.point1 = Point(1, 2)
        self.point2 = Point(-3, 1)
        self.point3 = Point(0, 10)

    def test_str(self):
        self.assertEqual(str(self.point1), '(1, 2)')
        self.assertEqual(str(self.point2), '(-3, 1)')

    def test_repr(self):
        self.assertEqual(repr(self.point1), 'Point(1, 2)')
        self.assertEqual(repr(self.point2), 'Point(-3, 1)')

    def test_eq(self):
        self.assertEqual(self.point1 == self.point1, True)
        self.assertEqual(self.point1 == Point(1, 2), True)
        self.assertEqual(self.point1 == self.point2, False)

    def test_ne(self):
        self.assertEqual(self.point1 != self.point2, True)
        self.assertEqual(self.point1 != Point(1, 2), False)
        self.assertEqual(self.point1 != self.point1, False)

    def test_add(self):
        self.assertEqual(self.point1 + self.point2, Point(-2, 3))
        self.assertEqual(self.point2 + self.point2, Point(-6, 2))
        self.assertEqual(self.point1 + self.point2 + self.point3, Point(-2, 13))

    def test_sub(self):
        self.assertEqual(self.point1 - self.point2, Point(4, 1))
        self.assertEqual(self.point2 - self.point2, Point(0, 0))
        self.assertEqual(self.point1 - self.point2 - self.point3, Point(4, -9))

    def test_mul(self):
        self.assertEqual(self.point1 * self.point2, -1)
        self.assertEqual(self.point2 * self.point2, 10)

    def test_cross(self):
        self.assertEqual(self.point1.cross(self.point2), 7)
        self.assertEqual(self.point2.cross(self.point2), 0)

    def test_length(self):
        self.assertEqual(self.point1.length(), math.sqrt(5))
        self.assertEqual(self.point2.length(), math.sqrt(10))
        self.assertEqual(self.point3.length(), 10)

if __name__ == '__main__':
    unittest.main()