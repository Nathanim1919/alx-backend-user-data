#!/usr/bin/env python3
"""Auth Class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
