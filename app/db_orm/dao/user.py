from db_orm import db_factory as df
from db_orm.db_model import User, UserAuth


def get_user_by_identifier(identifier, identify_type):
    session = df.db_session()
    ua = session.query(UserAuth).filter(UserAuth.identifier == identifier).filter(UserAuth.identity_type == identify_type).first()
    if ua:
        return ua.user_info
    return None
