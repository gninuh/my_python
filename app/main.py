# -*- coding:utf-8 -*-
import app_config as ac
from db_orm import db_factory as df  # 想要全局变量的修改全局有效，必须import模块，对模块内变量修改，使用时也需要引用模块，调用模块内变量
from db_orm.dao.register import register
from web_api import my_python_api as mp
from flask import Flask
from flask_restful import Api


ac.init_config()
df.init_engine_session_base(ac.connection_string, ac.connection_echo)
app = Flask(__name__)
api = Api(app)
api.add_resource(mp.User, '/u/<string:identifier>', '/u/<string:identifier>/<string:identify_type>')
api.add_resource(mp.Register, '/register')


def init_database():
    from db_orm import db_model as dm
    dm.create_table()


if __name__ == '__main__':

    # print('连接字符串是：%s' % ac.connection_string)  # 在Mac的VS中报错，编码问题
    # print('是否显示执行过程：%s' % str(ac.connection_echo))
    # init_database()  # 如果遇到'mysql'错误，尝试安装驱动pip install mysql-connector-python-rf 
    # register(ac.IdentyfyType.ACCOUNT, 'usertwo')
    app.run(debug=False)