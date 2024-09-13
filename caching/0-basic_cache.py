#!/usr/bin/env python3
"""
A class BasicCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Dictionary"""
    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] =  item

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key, None)