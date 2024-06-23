#!/usr/bin/python3
"""
The function defines a State class and a
Base class to work with MySQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the Class
        id (int): The State id of the Class
        name (str): The State name of the Class
        cities (:obj:`City`): The Cities belongs to State

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
