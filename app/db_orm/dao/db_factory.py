from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import connection_string
from app.config import connection_echo


_engine = create_engine(connection_string, echo=connection_echo)
db_session = sessionmaker(bind=_engine)
