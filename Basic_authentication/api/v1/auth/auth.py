#!/usr/bin/env python3
"""Create a class to manage the API authentication."""
from flask import request
from typing import TypeVar, List


class Auth:
    """_summary_
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, path: str, excluded_paths: List[str]) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
