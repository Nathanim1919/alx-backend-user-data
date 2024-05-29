#!/usr/bin/env python3
"""DB module
"""
from typing import Dict
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user

    def find_user_by(self, **kwargs: Dict[str, str]) -> User:
        """Find a user by specified attributes.

        Raises:
            error: NoResultFound: When no results are found.
            error: InvalidRequestError: When invalid query arguments are passed

        Returns:
            User: First row found in the `users` table.
        """
        session = self._session
        try:
            user = session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()
        # print("Type of user: {}".format(type(user)))
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update a user's attribute by using Id and key-value pair

        Args:
            user_id (int): User Id
            **kwargs: Arbitrary keyword arguments representing
                        the attribute to update and its new value

        Raises:
            ValueError: If user_id is not found
                        or invalid attribute is passed

        Returns:
            None
        """
        try:
            # Find the user by Id
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError("User with id {} not found".format(user_id))

        # Update the user's attribute
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError("Invalid attribute: {}".format(key))
            setattr(user, key, value)

        try:
            # Commit the session to the database
            self._session.commit()
            self.__session.refresh(user)

        except InvalidRequestError:
            # Raise ValueError if the attribute is invalid
            raise ValueError("Invalid attribute")

