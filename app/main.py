# -*- coding:utf-8 -*-
import app_config as ac
from db_orm import db_factory as df
from db_orm.dao.register import register


def init_database():
    from db_orm import db_model as dm
    dm.create_table()


if __name__ == '__main__':
    ac.init_config()
    df.init_engine_session_base(ac.connection_string, ac.connection_echo)
    print('连接字符串是：%s' % ac.connection_string)
    print('是否显示执行过程：%s' % str(ac.connection_echo))
    # init_database()
    register(ac.IdentyfyType.ACCOUNT, 'usertwo')
