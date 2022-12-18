# Marlena Gryt
# Python 2022/2023
# Zd 10.2

from stack import *
import unittest

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_is_full(self):
        self.assertFalse(self.stack.is_full())
        for i in range(10):
            self.stack.push(i)
        self.assertTrue(self.stack.is_full())

    def test_push(self):
        self.assertEqual(self.stack.n, 0)
        for i in range(10):
            self.stack.push(i)
            self.assertEqual(self.stack.n, i+1)
        with self.assertRaises(ValueError):
            self.stack.push(11)

    def test_pop(self):
        for i in range(10):
            self.stack.push(i)
        for i in reversed(range(10)):
            self.assertEqual(self.stack.pop(), i)
            self.assertEqual(self.stack.n, i)
        with self.assertRaises(ValueError):
            self.stack.pop()

if __name__ == '__main__':
    unittest.main()