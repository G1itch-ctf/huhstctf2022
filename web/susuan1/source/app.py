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
import json
import random
import re
from flask import Flask,session,request,redirect,url_for
from datetime import timedelta
from flask import render_template
import os

#产生随机数字
def Number(m,n):
    return str(random.randint(m,n))



#产生随机运算符号
def caculate_symbol():
    symbol =['+','-','×','÷']
    return str(random.choice(symbol))


#生成六位数题目
def Test():
    subject_all=""
    subject=""
    for x in range(0,10):
        symbol = caculate_symbol()
        subject +=(Number(100000,1000000) + symbol)


    subject_all =subject[0:-1] + "="

    return subject_all


#生成答案
def Answer(subject_all):


    c = re.sub('×',"*",subject_all)
    b = re.sub('÷',"/",c)
    question = re.sub("=","",b)
    answer =  str("%d" %(eval(question)))


    return answer



app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route("/")
def hello():

    if "level" not in session:
        session["level"]="1"
        session.permanent = True

    if session["level"]=="100":
        with open("/flag","r") as f :
            flag=f.read()
        return flag

    challenges=Test()
    session["anwser"]=Answer(challenges)
    print(session)

    return render_template("login.html",challenges=challenges,level=session['level'])



@app.route("/submit",methods=['GET'])
def submit():
    if "level" not in session:
        session["level"]="1"
        session.permanent = True

    useranwser=request.args.get('anwser')
    anwser=Answer(session["anwser"])

    if useranwser ==anwser:
        print("yes")
        session["level"]=str(int(session["level"])+1)

    return redirect('/')







if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
