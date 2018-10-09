from db_orm import db_factory as df
from db_orm.db_model import User, UserAuth


def register(identity_type, identity, credential='', nickname='', avatar=''):
    avatar = avatar or 'http://nicelooipc.imwork.net/p/avata.jpg'
    nickname = nickname or '小P同学'

    user = User(nickname=nickname, avatar=avatar)
    userauth = UserAuth(identity_type=identity_type, identifier=identity, credential=credential, user_info=user)

    session = df.db_session()
    session.add(user)
    session.add(userauth)

    session.commit()
    session.close()
