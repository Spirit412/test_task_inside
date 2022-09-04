import enum
from datetime import *

from fastapi.encoders import jsonable_encoder
from sqlalchemy.dialects import postgresql
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text, JSON, Boolean, DECIMAL, Date, Enum
from sqlalchemy.orm import relationship, backref
import uuid

from api.database.sqlalchemy_connection import Base
from sqlalchemy.dialects.postgresql import UUID

metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    password_digest = Column(String)

    #### RELATIONSHIP
    user_messages = relationship("Message", backref="users")


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
