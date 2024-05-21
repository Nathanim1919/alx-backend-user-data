#!/usr/bin/env python3
"""Auth Class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Auth Class"""

    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        """Require Auth"""
        if path is None or exclude_paths is None or exclude_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in exclude_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization Header"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Current User"""
        return None
