# -*- coding:utf-8 -*-
import configparser
import os


connection_string = ''
connection_echo = False

application_id = '9d5a3450aac19672a1c2c27b11934dbde1022d2013d3681b6c5b4ae6ceb087aa'
secret = '04fcf9e379aa3169b3ba76dd7e35ecacfce89094026efb2730e27f813139b964'
redirect_uri = 'http://127.0.0.1:5000/token'
response_type = 'code'

def init_config():
    global connection_string  # 想要给全局变量赋值，需要使用[global]关键字
    global connection_echo
    cf = configparser.ConfigParser()
    cf.read(os.path.abspath(os.path.join(os.getcwd(), 'config', 'config.ini')))
    connection_string = cf.get('db', 'connectionstr')
    connection_echo = cf.getboolean('db', 'echo')


class IdentyfyType(object):
    PHONE = 'phone'
    EMAIL = 'email'
    ACCOUNT = 'account'
    WECHAT = 'wechat'
    WEIBO = 'weibo'


if __name__ == '__main__':
    init_config()
    print('连接字符串是：%s' % connection_string)
    print('是否显示执行过程：%s' % str(connection_echo))
