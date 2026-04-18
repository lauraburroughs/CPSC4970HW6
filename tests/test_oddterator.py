import unittest
from module4.iterators import OddIterator

# Laura Burroughs
# CPSC 4970
# 3 April 2026
# Project 4

class TestOddIterator(unittest.TestCase):

    def test_odd_iterator(self):
        numbers = [2, 3, 7, 6, 12, 19]
        result = OddIterator(numbers)
        self.assertEqual(list(result), [3, 7, 19])

    def test_odd_iterator_all_even(self):
        numbers = [2, 4, 6, 10, 12, 18]
        result = OddIterator(numbers)
        self.assertEqual(list(result), [])

    def test_odd_iterator_all_odd(self):
        numbers = [3, 5, 7, 11, 13, 19]
        result = OddIterator(numbers)
        self.assertEqual(list(result), [3, 5, 7, 11, 13, 19])

    def test_odd_iterator_empty(self):
        numbers = []
        result = OddIterator(numbers)
        self.assertEqual(list(result), [])

    def test_odd_iterator_negatives(self):
        numbers = [-3, -2, -1, 0, 1, 2]
        result = OddIterator(numbers)
        self.assertEqual(list(result), [-3, -1, 1])


