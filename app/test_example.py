#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/5
# @Author  : liyaru
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
from app import db
db.create_all()