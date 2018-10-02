import time
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from base import Base
from base import next_id


class UserAuth(Base):
    __tablename__ = 'userauth'

    id = Column(String(50), primary_key=True, default=next_id)
    user_id = Column(String(50), ForeignKey('user.id'))
    identity_type = Column(String(10), nullable=False)
    identifier = Column(String, nullable=False)
    credential = Column(String)
    create_time = Column(Float, default=time.time)
    last_update = Column(Float, onupdate=time.time)
    last_login = Column(Float)

    user = relationship('User', uselist=False, back_populates='user')
