#!/usr/bin/env python3
"""
A class LIFOCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Caching"""
    def __init__(self):
        super().__init__()
        self.stack = [] #stack to keep track of insertion order (LIFO)

    def put(self, key, item):
        """
        Add the item to the cache_data dictionary with the key as the key.
        If key or item is None, do nothing.
        If the cache exceeds the maximum number of
        items, discard the most recent item (LIFO).
        """
        if key or item is None:
            return
        #Remove key if it already exists so that it can be re-added
        if self.cache_data:
            self.stack.remove(key)
        #Add new item to the cache and stack
        self.cache_data[key] = item
        self.stack.append(key)
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the last item from the stack (the most recent one)
            last_key = self.stack.pop()
            del self.cache_data[last_key]  # Remove it from cache_data
            print(f"DISCARD: {last_key}")  # Print the discarded key

    def get(self, key):
        """
        Retrieve the value associated with the key from cache_data.
        If key is None or key is not found, return None.
        """
        if key is None:
            return None
        self.cache_data.get(key, None)

