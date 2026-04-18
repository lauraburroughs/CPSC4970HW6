import unittest
from module4.identified_object import IdentifiedObject

# Laura Burroughs
# CPSC 4970
# 27 March 2026
# Project 3

class TestIdentifiedObject(unittest.TestCase):

    def test_equal_same_oid(self):
        obj1 = IdentifiedObject(1)
        obj2 = IdentifiedObject(1)
        self.assertEqual(obj1, obj2)

    def test_not_equal_same_oid(self):
        obj1 = IdentifiedObject(1)
        obj2 = IdentifiedObject(2)
        self.assertNotEqual(obj1, obj2)

    def test_none_oid(self):
        obj1 = IdentifiedObject(1)
        self.assertNotEqual(obj1, None)

if __name__ == '__main__':
    unittest.main()



