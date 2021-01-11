# -*- coding: utf-8 -*-
from app import app
#from models import User, Post, ROLE_USER, ROLE_ADMIN
from flask import Flask, render_template

#http://localhost:5000/user/li


name = 'Grey Li'
movies = [ {'title': 'My Neighbor Totoro', 'year': '1988'}, {'title': 'Dead Poets Society', 'year': '1989'}, {'title': 'A Perfect World', 'year': '1993'}, {'title': 'Leon', 'year': '1994'}, {'title': 'Mahjong', 'year': '1996'}, {'title': 'Swallowtail Butterfly', 'year': '1996'}, {'title': 'King of Comedy', 'year': '1999'}, {'title': 'Devils on the Doorstep', 'year': '1999'}, {'title': 'WALL-E', 'year': '2008'}, {'title': 'The Pork of Music', 'year': '2012'}, ]
message={'title':'liyaru',"age":20,}
@app.route('/')
@app.route('/index')
def index():
    #return 'hello world, hello flaskhhhhh'
    return render_template('index.html', name=name, movies=movies,message=message)

@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % name