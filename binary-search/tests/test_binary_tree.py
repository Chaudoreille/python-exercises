import pytest
from binary_search import binary_search

class TestBinaryTree:
    def test_whenNumberExists_shouldReturnTrue(self):
        # with
        haystack = [i for i in range(200)]

        # when
        first =  binary_search(haystack, 0)
        random_value1 = binary_search(haystack, 22)
        random_value2 = binary_search(haystack, 190)
        last = binary_search(haystack, 199)

        # then
        assert first
        assert random_value1
        assert random_value2
        assert last

    def test_whenNumberDoesNotExist_shouldReturnFalse(self):
        # with
        haystack = [i for i in range(200)]

        # when
        out_of_range1 = binary_search(haystack, -1)
        out_of_range2 = binary_search(haystack, 200)

        # then
        assert not out_of_range1
        assert not out_of_range2

    def test_whenStringExists_shouldReturnTrue(self):
        # with
        haystack = ("just", "another", "string", "tuple")

        # when
        first = binary_search(haystack, "just")
        random = binary_search(haystack, "another")
        last = binary_search(haystack, "tuple")

        # then
        assert first
        assert random
        assert last

    def test_whenStringDoesNotExist_shouldReturnFalse(self):
        # with
        haystack = ("just", "another", "string", "tuple")

        # when
        search_result = binary_search(haystack, "Hello")

        # then
        assert not search_result
