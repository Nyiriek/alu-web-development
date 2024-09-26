#!/usr/bin/env python3
"""
Create a SQLAlchemy model named User for
a database table named users (by using the
mapping declaration of SQLAlchemy)
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class User(Base):
    """
    Class User that inherits from Base
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
