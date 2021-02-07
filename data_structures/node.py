class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def __contains__(self, data):
        if self.data is not None:
            if data == self.data:
                return True
            elif data < self.data:
                if self.left:
                    return data in self.left
                else:
                    return False
            else:
                if self.right:
                    return data in self.right
                else:
                    return False
        else:
            return False

    def __str__(self):
        string = ""
        if self.left:
            string += str(self.left)+" "
        if self.data is not None:
            string += "["+str(self.data)+"]"
        if self.right:
            string += " "+str(self.right)
        return string

    def binary_search(self, data):
        pass

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self.data

    def insert(self, data):
        if self.data is not None:
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
        return self

    def remove(self, data):
        if self.data is not None:
            if data < self.data:
                if not self.left:
                    return self
                else:
                    self.left = self.left.remove(data)
            elif data > self.data:
                if not self.right:
                    return self
                else:
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

    # def balance(self):
    #     if self.left:
    #         self.left.balance()
    #     if self.right:
    #         self.right.balance()
