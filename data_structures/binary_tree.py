class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def binary_search(self, data):
        pass

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def remove(self, data):
        if self.data:
            if data < self.data:
                self.left = self.left.remove(data)
            elif data > self.data:
                self.right = self.right.remove(data)
            else:
                