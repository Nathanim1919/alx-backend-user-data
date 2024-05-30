#!/usr/bin/env python3
"""Auth module
"""

import bcrypt
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """Hash a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user
            Args:
                email: user email
                password: user password
            Returns:
                User object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass

        # if user does not exist, create a new user
        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a user login
            Args:
                email: user email
                password: user password
            Returns:
                True if the password is correct, False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
        except InvalidRequestError:
            return False

    def create_session(self, email: str) -> str:
        """Get Session Id
            Args:
                email: user email to find user and
                 assing the created sessionid
            Return:
                session_id as String
        """
        try:
            # find user by email
            user = self._db.find_user_by(email=email)

            # generate new session id
            session_id = _generate_uuid()

            # update the user and assign the session id
            self._db.update_user(user.id, session_id=session_id)

            # return the created session id
            return session_id
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
        except InvalidRequestError:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy session
            Args:
                user_id: Integer user id
            Return:
                None
        """
        if user_id is None:
            return None
        self._db.update_user(user_id, sesssion_id=None)

    def get_reset_password_token(self, email: str) -> str:
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError
        except InvalidRequestError:
            raise ValueError
