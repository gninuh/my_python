from flask import Flask, request
from flask_restful import Resource


def to_json(model, error_code=0):
    if error_code:
        return {"error_code": error_code, "error_message":get_error_message(error_code)}
    if not model:
        return {"error_code": error_code, "error_message":get_error_message(error_code)}
    json = {}
    for col in model._sa_class_manager.mapper.mapped_table.columns:
        json[col.name] = getattr(model, col.name)
    return json


def get_error_message(error_code):
    return {
        0: '未查找到相关数据',
        1: '操作失败'
    }.get(error_code, '操作失败')


class User(Resource):
    def get(self, identifier, identify_type=None):
        from db_orm.dao import user
        import app_config as ac
        from tools import re_tool

        res = None

        if identifier:
            if not identify_type:
                if re_tool.is_cellphone(identifier):
                    identify_type = ac.IdentyfyType.PHONE
                elif re_tool.is_email(identifier):
                    identify_type = ac.IdentyfyType.EMAIL
                else:
                    identify_type = ac.IdentyfyType.ACCOUNT
            res = user.get_user_by_identifier(identifier, identify_type)
        return to_json(res)


class Register(Resource):
    def post(self):
        from db_orm.dao.register import register

        identity_type = request.form['identity_type'] or ''
        identity = request.form['identity'] or ''
        credential = request.form['credential'] or ''
        nickname = request.form['nickname'] or ''
        avatar = request.form['avatar'] or ''

        res = register(identity_type, identity, credential=credential, nickname=nickname, avatar=avatar)
        if res:
            return {"message": "注册成功"}, 200
        else:
            return to_json(None, 1)