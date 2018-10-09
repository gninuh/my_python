from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


_engine = None
db_session = None


def init_engine_session_base(connection_string, connection_echo):
    global _engine
    global db_session
    _engine = create_engine(connection_string, echo=connection_echo)
    db_session = sessionmaker(bind=_engine)
