import pytest
from lru_cache import LRUCache

class TestLRUCache:
    def test_whenInsertedValue_shouldGetValue(self):
        # with
        cache = LRUCache(1)

        #when
        cache.insert("key1", "value1")
        value = cache.get("key1")

        # then
        assert value == "value1"

    def test_whenInsertedValueOverLimit_shouldOnlyReturnLastInsertedValue(self):
        # with
        cache = LRUCache(1)

        # when
        cache.insert("key1", "value1")
        cache.insert("key2", "value2")

        value1 = cache.get("key1")
        value2 = cache.get("key2")

        # then
        assert not value1
        assert value2 == "value2"

    def test_whenInsertedValues_shouldUpdateRecentlyUsedOnGet(self):
        # with
        cache = LRUCache(2)

        # when
        cache.insert("key1", "value1")
        cache.insert("key2", "value2")
        cache.get("key1")
        cache.insert("key3", "value3")

        value1 = cache.get("key1")
        value2 = cache.get("key2")
        value3 = cache.get("key3")


        # then
        assert cache.get("key1") == "value1"
        assert not cache.get("key2")
        assert cache.get("key3") == "value3"