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

if os.environ.get('Heroku'):
    run(host='0.0.0.0', port=os.environ.get('PORT'))
else:
    run(host='localhost', port=8080)

