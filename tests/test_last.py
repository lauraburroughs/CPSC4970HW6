import unittest
from module4.iterators import Last


# Laura Burroughs
# CPSC 4970
# 4 April 2026
# Project 4


class TestLast(unittest.TestCase):

    def test_normal_case(self):
        elements = [1, 2, 3, 4, 5, 6, 7, 8]
        count = 3
        result = list(Last(elements, count))
        self.assertEqual(result, [6, 7,8 ])

    def test_empty(self):
        elements = []
        count = 3
        result = list(Last(elements, count))
        self.assertEqual(result, [])

    def test_larger_than_count(self):
        elements = [1, 2, 3]
        count = 10
        result = list(Last(elements, count))
        self.assertEqual(result, [1, 2, 3])

    def test_count_is_zero(self):
        elements = [1, 2, 3]
        count = 0
        result = list(Last(elements, count))
        self.assertEqual(result, [])

    def test_negative_count(self):
        with self.assertRaises(ValueError):
            Last([1, 2, 3], -1)

    def test_not_a_list(self):
        elements = "thisisnotalist"
        count = 2
        result = list(Last(elements, count))
        self.assertEqual(result, ["s", "t"])
