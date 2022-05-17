# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :exp.py
# @File     :app
# @Date     :2022/4/6 20:23
# @Author   :penson
# @Email    :decentpenson@gmail.com
# @Software :PyCharm
-------------------------------------------------
"""

from flask import Flask,session,request,redirect
from datetime import timedelta
from flask import render_template
import os
from sympy import *
import random



def generate():

    min=  random.randint(1,5)

    max = random.randint(6, 9)

    t= random.randint(3, 9)

    c = random.randint(3, 10)
    c2= random.randint(3, 10)


    x = symbols("x")
    func_list=["**"]

    symbol_list=["+","-"]

    func=random.choice(func_list)
    symbol=random.choice(symbol_list)
    func_text=""
    anwser=0
    if symbol =="+":
        if func =="**":
            anwser= integrate(c * x ** t +c2 * x, (x, min, max))
            func_text= f"{c}x^{t}+{c2}x"
        elif func=="e":
            anwser = integrate(c * 2.7 ** x +c2 * x, (x, min, max))
            func_text=f"{c}e^x+{c2}x"
    elif symbol == "-":
        if func =="**":
            anwser= integrate( c * x ** t - c2 * x, (x, min, max))
            func_text= f"{c}x^{t}-{c2}x"
        elif func=="e":
            anwser = integrate(c * 2.7 ** x - c2 * x, (x, min, max))
            func_text=f"{c}e^x-{c2}x"

    challenges=f"\\[\\int_{min}^{max} ({func_text})dx \\]"

    return challenges,str(int(anwser))


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route("/")
def hello():

    if "level" not in session:
        session["level"]="1"
        session.permanent = True

    if session["level"]=="100":
        with open("/flag","r") as f:
            flag=f.read()
        return flag

    challenges,anwser=generate()
    print(challenges,anwser)
    print(session["level"])

    session["anwser"]=anwser

    return render_template("login.html",challenges=challenges,level=session['level'])



@app.route("/submit",methods=['GET'])
def submit():
    if "level" not in session:
        session["level"]="1"
        session.permanent = True

    useranwser=request.args.get('anwser')
    if "anwser" in session:
        anwser=session["anwser"]
        print(anwser)
    else:
         return redirect('/')
    if useranwser ==anwser:
        session["level"]=str(int(session["level"])+1)

    return redirect('/')







if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
