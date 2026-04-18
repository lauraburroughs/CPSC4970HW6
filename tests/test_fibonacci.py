import unittest
from module4.generators import fibonacci

# Laura Burroughs
# CPSC 4970
# 3 April 2026
# Project 4

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_first_five(self):
        it = fibonacci()
        result = [next(it) for i in range(5)]
        self.assertEqual(result, [1, 1, 2, 3, 5])

    def test_fibonacci_first_ten(self):
        it = fibonacci()
        result = [next(it) for i in range(10)]
        self.assertEqual(result, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_fibonacci_next_manual(self):
        it = fibonacci()

        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 1)
        self.assertEqual(next(it), 2)
        self.assertEqual(next(it), 3)

    def test_fibonacci_independent_iterators(self):
        it1 = fibonacci()
        it2 = fibonacci()

        self.assertEqual(next(it1), 1)
        self.assertEqual(next(it2), 1)
        self.assertEqual(next(it1), 1)
        self.assertEqual(next(it2), 1)