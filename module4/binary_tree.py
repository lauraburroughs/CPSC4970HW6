class BinaryTreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.parent = None
        self._left_child = left_child
        self._right_child = right_child
        if left_child:
            left_child.parent = self
        if right_child:
            right_child.parent = self

    @property
    def left_child(self):
        return self._left_child

    @property
    def right_child(self):
        return self._right_child


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, r):
        self._root = r

    def __iter__(self):
        return InOrderIterator(self)


class InOrderIterator:

    def __init__(self, tree):
        self.current = tree.root
        self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left_child

        if not self.stack:
            raise StopIteration

        node = self.stack.pop()
        value = node.value
        self.current = node.right_child

        return value


class PreOrderIterator:

    def __init__(self, tree):
        self.stack = []
        if tree.root is not None:
            self.stack.append(tree.root)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        node = self.stack.pop()
        value = node.value

        if node.right_child is not None:
            self.stack.append(node.right_child)

        if node.left_child is not None:
            self.stack.append(node.left_child)

        return value


class PostOrderIterator:
    def __init__(self, tree):
        self.stack = []
        self.last_visited = None

        if tree.root:
            self.stack.append(tree.root)

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            node = self.stack[-1]

            # going down the tree
            if self.last_visited is None or self.last_visited not in (node.left_child, node.right_child):

                # left first, then right
                if node.left_child:
                    self.stack.append(node.left_child)
                    continue

                if node.right_child:
                    self.stack.append(node.right_child)
                    continue

            # if coming back from the left, go right
            if self.last_visited == node.left_child:
                if node.right_child:
                    self.stack.append(node.right_child)
                    continue

            # if coming back from the right or 0 children are left to process
            self.stack.pop()
            self.last_visited = node
            return node.value

        raise StopIteration


# sample
if __name__ == '__main__':
    n1 = BinaryTreeNode("A")
    n2 = BinaryTreeNode("B")
    n3 = BinaryTreeNode("C", n1, n2)
    n4 = BinaryTreeNode("D")
    n5 = BinaryTreeNode("E", n4, n3)
    n6 = BinaryTreeNode("F", n5)
    n7 = BinaryTreeNode("G")
    n8 = BinaryTreeNode("H", n6, n7)
    tree = BinaryTree(n8)
    print(tree.root.value)
    print(tree.root.left_child.left_child.value)
