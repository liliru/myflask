#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5
# @Author  :
# @Site    : 
# @File    : models.py
# @Software: PyCharm
"""
数据库配置以及数据表
"""
from flask_sqlalchemy import SQLAlchemy
from mainactivity import login_manager, app
from werkzeug.security import check_password_hash
from conf.config import config
import os
from flask_login import UserMixin


app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:shl0528+-@127.0.0.1:3306' \
                                                  '/data_resource_managment'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = '123456'
app.debug = True

db = SQLAlchemy(app)

cfg = config[os.getenv('FLASK_CONFIG') or 'default']


class UserInfo(UserMixin, db.Model):
    __tablename__ = 'user_info'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), unique=True)
    user_pwd = db.Column(db.String(100))
    file_email = db.Column(db.String(100), unique=True)
    company = db.Column(db.String(100))
    user_right = db.Column(db.Integer)

    def verify_password(self, raw_password):
        return check_password_hash(self.user_pwd, raw_password)

    def get_id(self):
        return self.user_id

    @staticmethod
    def get(user_id):
        if not user_id:
            return None
        try:
            return UserInfo()
        except:
            return None


@login_manager.user_loader
# @user_loader回调， 这个回调从会话中存储的用户 ID 重新加载用户对象，
# 它应该接受一个用户的 unicodeID 作为参数，并且返回相应的用户对象。
# 如果 ID 无效的话，它应该返回None (而不是抛出异常)。(
# 在这种情况下，ID 会被手动从会话中移除且处理会继续)
# load_user( )用来返回用户唯一标识
def load_user(user_id):
    return UserInfo.get(user_id)
