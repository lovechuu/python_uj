# Marlena Gryt
# Python 2022/2023
# Zd 10.8

from random_queue import *
import unittest

class TestRandomQueue(unittest.TestCase):
    def setUp(self):
        self.queue = RandomQueue()

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.insert(1)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        for i in range(10):
            self.queue.insert(i)
        self.assertTrue(self.queue.is_full())

    def test_insert(self):
        self.assertEqual(len(self.queue.items), 0)
        for i in range(1, 11):
            self.queue.insert(i)
            self.assertEqual(len(self.queue.items), i)
        with self.assertRaises(ValueError):
            self.queue.insert(11)

    def test_remove(self):
        for i in range(10):
            self.queue.insert(i)
        for i in reversed(range(10)):
            self.queue.remove()
            self.assertEqual(len(self.queue.items), i)
        with self.assertRaises(ValueError):
            self.queue.remove()

        def test_clear(self):
            for i in range(10):
                self.queue.insert(i)
            self.assertFalse(self.queue.is_empty())
            self.queue.clear()
            self.assertTrue(self.queue.is_empty())

if __name__ == '__main__':
    unittest.main()