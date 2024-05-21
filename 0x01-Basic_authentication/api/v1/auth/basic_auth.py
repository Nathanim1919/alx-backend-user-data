#!/usr/bin/env python3
"""Basic Auth module
"""
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic Auth class
    """

#     def extract_base64_authorization_header(
#             self, authorization_header: str) -> str:
#         """Extract base64 authorization header
#         """
#         if authorization_header is None or not isinstance(
#                 authorization_header, str):
#             return None
#         if not authorization_header.startswith("Basic "):
#             return None
#         return authorization_header[6:]

#     def decode_base64_authorization_header(
#             self, base64_authorization_header: str) -> str:
#         """Decode base64 authorization header
#         """
#         if base64_authorization_header is None or not isinstance(
#                 base64_authorization_header, str):
#             return None
#         try:
#             return base64_authorization_header.encode('utf-8').decode(
#                 'base64')
#         except BaseException:
#             return None

#     def extract_user_credentials(
#             self, decoded_base64_authorization_header: str) -> (str, str):
#         """Extract user credentials
#         """
#         if decoded_base64_authorization_header is None or not isinstance(
#                 decoded_base64_authorization_header, str):
#             return (None, None)
#         if ':' not in decoded_base64_authorization_header:
#             return (None, None)
#         return tuple(decoded_base64_authorization_header.split(':', 1))

#     def user_object_from_credentials(
#             self, user_email: str, user_pwd: str) -> TypeVar('User'):
#         """User object from credentials"""
#         if user_email is None or not isinstance(user_email, str):
#             return None
#         if user_pwd is None or not isinstance(user_pwd, str):
#             return None

#         try:
#             users = User.search({'email': user_email})
#         except Exception:
#             return None
#         if len(users) == 0:
#             return None
#         if users[0].is_valid_password(user_pwd):
#             return users[0]

#     def current_user(self, request=None) -> TypeVar('User'):
#         """Current user"""
#         auth_header = self.authorization_header(request)
#         base64_auth_header = self.extract_base64_authorization_header(
#             auth_header)
#         decoded_base64_auth_header = self.decode_base64_authorization_header(
#             base64_auth_header)
#         user_credentials = self.extract_user_credentials(
#             decoded_base64_auth_header)
#         user = self.user_object_from_credentials(
#             user_credentials[0], user_credentials[1])
#         return user
