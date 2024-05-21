#!/usr/bin/env python3
"""Basic Auth module
"""
from .auth import Auth
from models.user import User
from typing import TypeVar, Tuple


class BasicAuth(Auth):
    """Basic Auth class
    """
