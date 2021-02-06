class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def binary_search(self, data):
        pass

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data

    def max(self):
        if self.right:
            return self.right.min()
        else:
            return self.data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
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
                if not self.left and not self.right:
                    return None
                elif self.right:
                    self.data = self.right.min()
                    self.right = self.right.remove(self.data)
                else:
                    self.data = self.left.max()
                    self.left = self.left.remove(self.data)
        return self
                    
    def height(self):
        if not self.left and not self.right:
            return 1
        elif not self.right:
            return self.left.height + 1
        elif not self.left:
            return self.right.height + 1
        else:
            return max(self.left.height(), self.right.height()) + 1

 