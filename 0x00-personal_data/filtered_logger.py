#!/usr/bin/env python3
"""Filtering module"""
import re
import logging


def filter_datum(fields: str, redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(rf'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
