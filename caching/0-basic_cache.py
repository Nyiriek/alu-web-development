#!/usr/bin/env python3
"""
A class BasicCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Dictionary"""
    def put(self, key, item):
        """
        Add the item to the cache_data dictionary with the key as the key.
        If key or item is None, do nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the key from cache_data.
        If key is None or key is not found, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
