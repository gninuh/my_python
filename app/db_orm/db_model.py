import time
from sqlalchemy import Column, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from tools.uuid_tool import next_id
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserAuth(Base):
    __tablename__ = 'userauth'

    id = Column(String(50), primary_key=True, default=next_id)
    user_id = Column(String(50), ForeignKey('user.id'))
    identity_type = Column(String(10), nullable=False)
    identifier = Column(String(50),  primary_key=True)
    credential = Column(Text)
    create_time = Column(Float, default=time.time)
    last_update = Column(Float, onupdate=time.time)
    last_login = Column(Float)

    user_info = relationship('User')


class User(Base):
    __tablename__ = 'user'

    id = Column(String(50), primary_key=True, default=next_id)
    nickname = Column(String(20), nullable=False)
    avatar = Column(Text)
    create_time = Column(Float, default=time.time)
    last_update = Column(Float, onupdate=time.time)
    last_login = Column(Float)

    auths = relationship('UserAuth', back_populates='user_info')


def create_table():
    from db_orm import db_factory as df
    Base.metadata.drop_all(df._engine)
    Base.metadata.create_all(df._engine)