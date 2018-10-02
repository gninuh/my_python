import time
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from base import Base
from base import next_id


class User(Base):
    __tablename__ = 'user'

    id = Column(String(50), primary_key=True, default=next_id)
    nickname = Column(String(20), nullable=False)
    avatar = Column(String)
    create_time = Column(Float, default=time.time)
    last_update = Column(Float, onupdate=time.time)
    last_login = Column(Float)

    auths = relationship('UserAuth', back_populates='userauth')
