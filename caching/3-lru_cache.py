#!/usr/bin/env python3
"""
A class LRUCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching"""
    def __init__(self):
        super().__init__()
        self.usage_order = [] # Holds keys for LRU tracking
        
    
    def put(self, key, item):
        """
        Add the item to the cache_data dictionary with the key as the key.
        If key or item is None, do nothing.
        If the cache exceeds the maximum number of items, discard the least
        Recently used item (LRU)
        """
        if key or item is None:
            return
        #Remove key if it already exists so that it can be re-added
        if self.cache_data:
            self.stack.remove(key)
        # Add key value pair to the cache and record its usage
        self.cache_data[key] = item
        self.cache_data.append(key)
        # Remove the least recently used item (first in the order list) if the cache exceeds the max-size
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.usage_order.pop(0)  # Remove the least recently used key (first in the list)
            del self.cache_data[lru_key]  # Remove it from the cache
            print(f"DISCARD: {lru_key}")  # Print the discarded key

    def get(self, key):
        """
        Retrieve the value associated with the key from cache_data.
        If key is None or key is not found, return None.
        If the key exists, update its position in the usage order to mark it as recently used.
        """
        if key is None or key not in self.cache_data:
            return None
        #Mark the key as recently used by moving it to the end of the usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)

        return self.cache_data(key)