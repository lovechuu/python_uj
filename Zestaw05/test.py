from polys import *
import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]            # W(x) = x
        self.p2 = [0, 0, 1]         # W(x) = x^2
        self.p3 = [2, 2, 2]         # W(x) = 2x^2 + 2x + 2 
        self.p4 = [-2, -2, -2]      # W(x) = -2x^2 - 2x - 2 
        self.p5 = [0, 1, 0]         # W(x) = x 

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])      # W(x) = x^2 + x
        self.assertEqual(add_poly(self.p2, self.p3), [2, 2, 3])      # W(x) = 3x^2 + 2x + 2
        self.assertEqual(add_poly(self.p3, self.p4), [0])            # W(x) = 0

    def test_sub_poly(self): 
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])     # W(x) = -x^2 + x 
        self.assertEqual(sub_poly(self.p2, self.p3), [-2, -2, -1])   # W(x) = -x^2 - 2x - 2
        self.assertEqual(sub_poly(self.p3, self.p4), [4, 4, 4])      # W(x) = 4x^2 + 4x + 4

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])              # W(x) = x^3
        self.assertEqual(mul_poly(self.p2, self.p3), [0, 0, 2, 2, 2])           # W(x) = 2x^4 + 2x^3 + 2x^2 
        self.assertEqual(mul_poly(self.p3, self.p4), [-4, -8, -12, -8, -4])     # W(x) = -4x^4 - 8x^3 - 12x^2 - 8x - 4

    def test_is_zero(self): 
        self.assertEqual(is_zero([0]), True)
        self.assertEqual(is_zero([0, 0, 0]), True)
        self.assertEqual(is_zero(self.p1), False)

    def test_eq_poly(self): 
        self.assertEqual(eq_poly(self.p1, self.p1), True)
        self.assertEqual(eq_poly(self.p3, self.p4), False)
        self.assertEqual(eq_poly(self.p1, self.p5), True)

    def test_eval_poly(self): 
        self.assertEqual(eval_poly(self.p1, 3), 3)
        self.assertEqual(eval_poly(self.p2, 2), 4)
        self.assertEqual(eval_poly(self.p3, 1), 6)
        self.assertEqual(eval_poly(self.p4, 0), -2)

    def test_combine_poly(self): 
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])             # W(x) = x^2
        self.assertEqual(combine_poly(self.p2, self.p3), [4, 8, 12, 8, 4])      # W(x) = 4x^4 + 8x^3 + 12x^2 + 8x+ 4  
        self.assertEqual(combine_poly(self.p3, self.p4), [6, 12, 20, 16, 8])    # W(x) = 8x^4 + 16x^3 + 20x^2 + 12x + 6

    def test_pow_poly(self): 
        self.assertEqual(pow_poly(self.p1, 3), [0, 0, 0, 1])        # W(x) = x^3
        self.assertEqual(pow_poly(self.p2, 2), [0, 0, 0, 0, 1])     # W(x) = x^4
        self.assertEqual(pow_poly(self.p3, 1), [2, 2, 2])           # W(x) = 2x^2 + 2x + 2
        self.assertEqual(pow_poly(self.p4, 0), [1])                 # W(x) = 1

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])             # (x)' = 1
        self.assertEqual(diff_poly(self.p2), [0, 2])          # (x^2)' = 2x
        self.assertEqual(diff_poly(self.p3), [2, 4])          # (2x^2 + 2x + 2)' = 4x + 2
        self.assertEqual(diff_poly(self.p4), [-2, -4])        # (-2x^2 - 2x - 2)' = -4x - 2 

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy