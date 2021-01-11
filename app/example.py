#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 17:24
# @Author  : 孙海龙
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

class Movie(db.Model):
    # 表名将会是 movive
    id = db.Column(db.Integer, primary_key=True) # 主键
    title = db.Column(db.String(60)) # 电影标题
    year = db.Column(db.String(4)) # 电影年份



