# -*- coding:utf-8 -*-
import configparser
import os


connection_string = ''
connection_echo = False


def init_config():
    global connection_string  # 想要给全局变量赋值，需要使用[global]关键字
    global connection_echo
    cf = configparser.ConfigParser()
    cf.read(os.path.abspath(os.path.join(os.getcwd(), 'config', 'config.ini')))
    connection_string = cf.get('db', 'connectionstr')
    connection_echo = cf.get('db', 'echo')


class IdentyfyType(object):
    PHONE = 'phone'
    EMAIL = 'email'
    ACCOUNT = 'account'
    WECHAT = 'wechat'
    WEIBO = 'weibo'


if __name__ == '__main__':
    init()
    print('连接字符串是：%s' % connection_string)
    print('是否显示执行过程：%s' % str(connection_echo))
