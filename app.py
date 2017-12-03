import os
from bottle import *

@route('/static/<skraarnafn>')
def static_skrar(skraarnafn):
    return static_file(skraarnafn, root='./static')

@route("/")
def index():
    return template("forsida.tpl")




@route("/eyda")
def eyda():
    Kerra.clear()
    redirect("/")

@route('/kostnadur')
def index():
    return template('kostnadur.tpl')


@route('/kostnadur2', method='POST')
def kostnadur2():
    nafn = request.forms.get('nafn')
    hf = request.forms.get('hf')
    mail = request.forms.get('mail')
    simi = request.forms.get('simi')
    kort = request.forms.get('kort')
    return "<link rel='stylesheet' type='text/css' href='static/css.css'>" \
           "<h1>Takk fyrir að velja þessa síðu</h1>" \
           "<br>", "Nafn: " , nafn, "<br>", "Heimilisfang: " , hf, "<br>" \
           "Netfang: ",  mail, "<br>", "Simi: ", simi, "<br>" \
           "Kort: " , kort, "<br><br>" \
           "<a href='/kostnadur'>Til baka</a><br><br>" \
           "<a href='/'>Forsíða</a>"
            

             

Kerra = []
@route("/add/<item>")
def add(item):
        Kerra.append(item)
        redirect("/")

@route("/kerra")
def kerra():
    bla = ["<br>"]
    sam = 0
    for i in Kerra:
        if i == "hondashadow":
            bla.append("Honda Shadow Spirit 700.000 kr")
            sam = sam + 700000
        elif i == "kawasakivulcan":
            bla.append("Kawasaki Vulcan 800 650.000 kr")
            sam = sam + 650000
        elif i == "yamahaxv":
            bla.append("Yamaha XV 1100 Virago 470.000 kr")
            sam = sam + 470000
        elif i == "suzukintruder":
            bla.append("Suzuki Intruder 580.000 kr")
            sam = sam + 580000
        elif i == "yamaha":
            bla.append("Yamaha Stratoliner 1.890.000 kr")
            sam = sam + 1890000
        elif i == "yamadavstar":
            bla.append("Yamaha V Star 650.000 kr")
            sam = sam + 650000
        elif i == "yamahavirgo":
            bla.append("Yamaha Virgo 720.000 kr")
            sam = sam + 720000
        elif i == "img6267":
            bla.append("IMG_6267 750.000 kr")
            sam = sam + 750000
    kerra = '<br>'.join(bla)
    sam1 = str(sam)
    return "<link rel='stylesheet' type='text/css' href='static/css.css'>" \
            "---------------------------------------------------<br>" \
            "Kerra þín", kerra, "<br><br>" \
            "Samtals "  , sam1 , " Kr<br><br>"\
            "<a href='/kostnadur'>------Borga------</a><br><br>" \
            "---------------------------------------------------<br>" \
            "Smelltu á <a href='/eyda'>Þennan</a> knppa til að eyða vörunum úr listanum<br><br>" \
            "Smelltu á <a href='/'>Þennan</a> knappa til að fara til baka"


run(host='0.0.0.0', port=os.environ.get('PORT'))
