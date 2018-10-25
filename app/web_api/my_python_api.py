from flask import Flask, request, redirect, url_for
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


class Login(Resource):
    def get(self):
        from app_config import application_id, redirect_uri, response_type
        # return redirect(url_for('http://192.168.0.2:3080/oauth/authorize', client_id=application_id, redirect_uri=redirect_uri, response_type=response_type)) 
        return redirect('http://192.168.0.2:3080/oauth/authorize?client_id=9d5a3450aac19672a1c2c27b11934dbde1022d2013d3681b6c5b4ae6ceb087aa&redirect_uri=http://127.0.0.1:5000/token&response_type=code')


class Token(Resource):
    def get(self):
        from app_config import application_id, secret, response_type
        import requests
        headers = {'Content-Type': 'multipart/form-data'}
        code = request.args.get('code') or ''
        payload = {"client_id": application_id, 'client_secret': secret, 'grant_type' : 'authorization_code', 'code' : code}
        r = requests.post('http://192.168.0.2:3080/oauth/access_token', headers=headers, data=payload )
        # access_token = request.form['access_token'] or ''
        # token_type = request.form['token_type'] or ''
        # expires_in = request.form['expires_in'] or ''
        # refresh_token = request.form['refresh_token'] or ''
        # return {'access_token' : access_token , 'token_type' : token_type, 'expires_in' : expires_in , 'refresh_token' : refresh_token}
        return r.content