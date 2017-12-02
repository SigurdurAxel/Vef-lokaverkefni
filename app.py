import os
from bottle import *

@route('/static/<skraarnafn>')
def static_skrar(skraarnafn):
    return static_file(skraarnafn, root='./static')

@route("/")
def index():
    return template("forsida.tpl")

kerra = []
@route("/add/<item>")
def add(item):
        kerra.append(item)
        redirect("/")

run(host='localhost', port=8080)
