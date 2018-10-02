import time
import uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # 创建基类


def next_id() -> str:  # 生成UDID做唯一标识
    """生成时间+UUID做唯一标识
    """
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
