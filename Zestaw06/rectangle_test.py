# Marlena Gryt
# Python 2022/2023
# Zd 6.3

import unittest
from rectangle import *

# Kod testujacy modul.
class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(0, 0, 4, 4)
        self.rect2 = Rectangle(-6, -5, -4, -1.25)

    def test_str(self):
        self.assertEqual(str(self.rect1), '[(0, 0), (4, 4)]')
        self.assertEqual(str(self.rect2), '[(-6, -5), (-4, -1.25)]')
    
    def test_repr(self):
        self.assertEqual(repr(self.rect1), 'Rectangle(0, 0, 4, 4)')
        self.assertEqual(repr(self.rect2), 'Rectangle(-6, -5, -4, -1.25)')

    def test_eq(self):
        self.assertEqual(self.rect1 == self.rect1, True)
        self.assertEqual(self.rect1 == Rectangle(0, 0, 4, 4), True)
        self.assertEqual(self.rect1 == self.rect2, False)

    def test_ne(self):
        self.assertEqual(self.rect1 != self.rect1, False)
        self.assertEqual(self.rect1 != Rectangle(0, 0, 4, 4), False)
        self.assertEqual(self.rect1 != self.rect2, True)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2, 2))
        self.assertEqual(self.rect2.center(), Point(-5.0, -3.125))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 16)
        self.assertEqual(self.rect2.area(), 7.5)

    def test_move(self):
        self.assertEqual(self.rect1.move(1, 1), Rectangle(1, 1, 5, 5))
        self.assertEqual(self.rect2.move(-1, -3), Rectangle(-7, -8, -5, -4.25))

if __name__ == '__main__':
    unittest.main()