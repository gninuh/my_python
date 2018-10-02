from model.base import Base
from dao.db_factory import _engine
# from model.user import User
# from model.user_auth import UserAuth


def create_table():
    Base.metadata.create_all(_engine)
