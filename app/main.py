# -*- coding:utf-8 -*-
import config
from db_orm.init_table import create_table

if __name__ == '__main__':
    config.init_config()
    print('连接字符串是：%s' % config.connection_string)
    print('是否显示执行过程：%s' % str(config.connection_echo))
    create_table()
