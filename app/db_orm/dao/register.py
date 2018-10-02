from db_factory import db_session
from app.orm.model.user import User
from app.orm.model.user_auth import UserAuth


def register(identity_type, identity, credential='', nickname='', avatar=''):
    avatar = avatar or 'http://nicelooipc.imwork.net/p/avata.jpg'
    nickname = nickname or '小P同学'

    user = User(nickname=nickname, avatar=avatar)
    userauth = UserAuth(identity_type=identity_type, identity=identity, credential=credential, user=user)

    session = db_session()
    session.add(user)
    session.add(userauth)

    session.commit()
    session.close()
