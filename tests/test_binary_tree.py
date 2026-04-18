import unittest
from module4.binary_tree import (
    BinaryTree, BinaryTreeNode, InOrderIterator,
    PreOrderIterator, PostOrderIterator
)

# Laura Burroughs
# CPSC 4970
# 3 April 2026
# Project 4

class TestBinaryTreeIterators(unittest.TestCase):

    def build_tree(self):
        n1 = BinaryTreeNode("A")
        n2 = BinaryTreeNode("B")
        n3 = BinaryTreeNode("C", n1, n2)
        n4 = BinaryTreeNode("D")
        n5 = BinaryTreeNode("E", n4, n3)
        n6 = BinaryTreeNode("F", n5)
        n7 = BinaryTreeNode("G")
        n8 = BinaryTreeNode("H", n6, n7)
        return BinaryTree(n8)

    def test_inorder_for_loop(self):
        tree = self.build_tree()
        result = []

        for value in tree:
            result.append(value)

        self.assertEqual(result, ["D", "E", "A", "C", "B", "F", "H", "G"])

    def test_inorder_iterator(self):
        tree = self.build_tree()
        it = InOrderIterator(tree)

        result = []
        for value in it:
            result.append(value)

        self.assertEqual(result, ["D", "E", "A", "C", "B", "F", "H", "G"])

    def test_preorder_iterator(self):
        tree = self.build_tree()
        it = PreOrderIterator(tree)
        result = list(it)
        self.assertEqual(result, ["H", "F", "E", "D", "C", "A", "B", "G"])

    def test_postorder_iterator(self):
        tree = self.build_tree()
        it = PostOrderIterator(tree)
        result = list(it)
        self.assertEqual(result, ["D", "A", "B", "C", "E", "F", "G", "H"])

    def test_empty_tree(self):
        tree = BinaryTree()
        result = list(tree)
        self.assertEqual(result, [])

    def test_single_node(self):
        node = BinaryTreeNode("A")
        tree = BinaryTree(node)

        self.assertEqual(list(tree), ["A"])
        self.assertEqual(list(PreOrderIterator(tree)), ["A"])
        self.assertEqual(list(PostOrderIterator(tree)), ["A"])

    def test_next_manual(self):
        tree = self.build_tree()
        it = InOrderIterator(tree)
        result = []
        try:
            while True:
                result.append(next(it))
        except StopIteration:
            pass
        self.assertEqual(result, ["D", "E", "A", "C", "B", "F", "H", "G"])

    def test_postorder_left_skewed(self):
        n3 = BinaryTreeNode("C")
        n2 = BinaryTreeNode("B", n3, None)
        n1 = BinaryTreeNode("A", n2, None)
        tree = BinaryTree(n1)

        result = list(PostOrderIterator(tree))
        self.assertEqual(result, ["C", "B", "A"])

    def test_postorder_right_skewed(self):
        n3 = BinaryTreeNode("A")
        n2 = BinaryTreeNode("B", None, n3)
        n1 = BinaryTreeNode("C", None, n2)
        tree = BinaryTree(n1)

        result = list(PostOrderIterator(tree))
        self.assertEqual(result, ["A", "B", "C"])

    def test_postorder_zigzag(self):
        n3 = BinaryTreeNode("C")
        n2 = BinaryTreeNode("B", None, n3)
        n1 = BinaryTreeNode("A", n2, None)
        tree = BinaryTree(n1)

        result = list(PostOrderIterator(tree))
        self.assertEqual(result, ["C", "B", "A"])