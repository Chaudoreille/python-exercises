import unittest
from .binary_tree import BinaryTree

class BinaryTreeMethods(unittest.TestCase):
    def test_insert(self):
        tree = BinaryTree(10)