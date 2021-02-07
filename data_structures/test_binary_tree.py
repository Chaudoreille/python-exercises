import unittest
from node import Node

class BinaryTreeMethods(unittest.TestCase):
    def test_insert(self):
        tree = Node()
        data=range(10)

        for element in data:
            tree = tree.insert(element)
            self.assertTrue(tree)

    def test_str(self):
        tree = Node(10)
        tree = tree.insert(5)
        tree = tree.insert(18)
        self.assertEqual("[5] [10] [18]", str(tree))

    def test_in(self):
        tree = Node()

        for element in range(10):
            tree = tree.insert(element)
            self.assertTrue(element in tree)

    def test_max(self):
        tree = Node()
        treeverse = Node()

        for element in range(10):
            tree = tree.insert(element)
            self.assertTrue(tree.max() == element)

        for element in range(9,-1,-1):
            treeverse = treeverse.insert(element)
            self.assertTrue(treeverse.max() == 9)

    def test_min(self):
        tree = Node()
        treeverse = Node()

        for element in range(10):
            tree = tree.insert(element)
            self.assertTrue(tree.min() == 0)

        for element in range(9,-1,-1):
            treeverse = treeverse.insert(element)
            self.assertTrue(treeverse.min() == element)

    def test_remove(self):
        tree = Node(10)
        tree.insert(5)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree.insert(3)

        self.assertTrue(8 in tree)
        tree = tree.remove(8)
        self.assertFalse(8 in tree)
        self.assertTrue(3 in tree)
        tree = tree.remove(3)
        self.assertFalse(3 in tree)
        self.assertTrue(10 in tree)
        tree = tree.remove(10)
        self.assertFalse(10 in tree)
        tree = tree.remove(10)
        self.assertFalse(10 in tree)

if __name__ == "__main__":
    unittest.main()
