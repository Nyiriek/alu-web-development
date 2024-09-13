#!/usr/bin/env python3
"""
A class MRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching"""
    def __init__(self):
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Add the item to the cache_data dictionary with the key as the key.
        If key or item is None, do nothing.
        If the cache exceeds the maximum number of items, discard the most
        recently used item (MRU).
        """
        if key or item is None:
            return
        # Remove the key from the usage order if it already exists ansd re-add it to the end
        if key in self.cache_data:
            self.usage_order.remove(key)

        # Add key value pair to cache and record its usage
        self.cache_data[key] = item
        self.usage_order.append(key)

        # Remove the most recently used item (last in the order list) if cache exceeds max size
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Retrieve the value associated with the key from cache_data.
        If key is None or key is not found, return None.
        If the key exists, update its position in the usage order
        to mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark the key as recently used by moving it to the end of the usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data[key]
