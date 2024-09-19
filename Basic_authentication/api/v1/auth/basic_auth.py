#!/usr/bin/env python3
"""
Create a class BasicAuth that inherits from Auth.
For the moment this class will be empty.
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """_summary_

        Args:
            authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if authorization_header is None or \
           type(authorization_header) is not str or \
           not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """_summary_

        Args:
            base64_authorization_header (str): _description_

        Returns:
            str: _description_
        """
        if base64_authorization_header is None or \
           type(base64_authorization_header) is not str:
            return None
        try:
            decoded_bytes = base64_authorization_header.encode('utf-8')
            return base64.b64decode(decoded_bytes).decode('utf-8')
        except (base64_authorization_header.binascii.Error,
                UnicodeDecodeError):
            return None
