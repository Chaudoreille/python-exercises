from collections import deque

class CacheNode:
    def __init__(self, key, data, previous=None, next=None):
        self.key = key
        self.data = data
        self.previous = previous
        self.next = next

        if self.previous:
            self.previous.next = self
        if self.next:
            self.next.previous = self

    def remove(self):
        if self.next:
            self.next.previous = self.previous
        if self.previous:
            self.previous.next = self.next


class LRUCache:
    def __init__(self, max_size):
        self.first = None
        self.last = None
        self.max_size = max_size
        self.repository = {}

    def get(self, key):
        node = self.repository.get(key, None)

        if not node:
            return None

        self._push(key, node.data)

        return node.data

    def insert(self, key, value):
        node = self.repository.get(key, None)

        if not node and len(self.repository) == self.max_size:
            self._pop()

        self._push(key, value)

        if not self.first:
            self.first = self.last

    def _push(self, key, data):
        node = self.repository.get(key, None)

        if node:
            node = self._unlink_node(key)

        self.last = CacheNode(key, data, self.last)
        self.repository[key] = self.last

    def _unlink_node(self, key):
        node = self.repository[key]

        if self.first == node:
            self.first = node.next
        if self.last == node:
            self.last = node.previous

        node.remove()

        return node

    def _pop(self):
        if self.first:
            unlinked_node = self._unlink_node(self.first.key)
            del self.repository[unlinked_node.key]
