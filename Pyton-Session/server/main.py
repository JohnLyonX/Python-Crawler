from flask import Flask, request, render_template, make_response
import json
import numpy as np

app = Flask(__name__, template_folder="temps")

COOKIEID = f'skysinsadfasdfasdfasdfsadfsskdind'


@app.route("/login")
def login():
    return render_template("login.html")


# 登陆认证
@app.route("/auth", methods=['POST'])
def auth():
    # 获取前端传来的参数
    user = request.form.get('user')
    password = request.form.get('pwd')
    if user == 'LyonJohn' and password == '123':
        # 写Cookie
        resp = make_response('success!')
        resp.set_cookie("login_id", COOKIEID)
        return resp
    else:
        return "fail!"


@app.route("/")
def index():
    login_id = request.cookies.get('login_id')
    if login_id == COOKIEID:
        return render_template("index.html")
    return "请登陆"


@app.route("/books")
def books():
    data = json.dumps(["西游记", "三国演义", "水浒传", "金瓶梅"], ensure_ascii=False)
    return data


app.run()
