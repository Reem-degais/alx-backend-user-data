#!/usr/bin/env python3
"""
 function called filter_datum that returns the log message
"""

from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Return an obfuscated log message.
    arg:
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line separator
    """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
