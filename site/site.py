import json
import random
import threading
import os
import time
import pymysql
import hashlib
import uuid
import datetime
from flask_cors import CORS
from flask.helpers import url_for
from flask import Flask, render_template, request, session, Response, make_response, redirect, jsonify, abort
import sys
# sys.path.insert(0, "../neyron")
# print(sys.path)
import neyronka_s

# import neyronka_s

application = Flask(__name__)

code_API = []
CORS(application)


class DB():
    """Работа с Базой данных
    получить данные::

        DB.GET('Текст запроса SQL')
    отправить данные::

        DB.POST('Текст запроса SQL')
    """

    def GET(self):
        """Получает данные с Базы данных
        """
        connection = pymysql.connect(host="31.31.196.245", user='u0981115',
                                     password='qwert5656', database='u0981115_itsunrise', charset="utf8mb4")
        cursor = connection.cursor()
        cursor.execute(self)
        OTV = cursor.fetchall()
        return(OTV)

    def POST(self):
        """Отправляет данные в Базу данных
        """
        connection = pymysql.connect(host="31.31.196.245", user='u0981115',
                                     password='qwert5656', database='u0981115_itsunrise', charset="utf8")
        cursor = connection.cursor()
        cursor.execute(self)
        connection.commit()
        return('True')


@application.route('/')
def index():
    # Вывод страницы
    return render_template("index_.html")


@application.route('/auth')
def auth():
    # Вывод страницы
    return render_template("auth.html")


@application.route('/track')
def track():
    # Вывод страницы
    return render_template("track.html")


@application.route('/test')
def test():
    # Вывод страницы
    return render_template("test.html")


@application.route('/cr')
def cr():
    # Вывод страницы
    return render_template("cr.html")


@application.route('/api/0.1/neyrondata', methods=["POST"])
def neyrondata():
    response_data = request.data.decode()
    print("data", response_data)
    response_data = json.loads(response_data)
    # print()
    # [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0]
    response_data = {"word": neyronka_s.get_data(response_data["neyron"])}
    return response_data, 200


@application.route('/api/0.1/get_prof', methods=["POST"])
def get_prof():
    # response_data = request.data.decode()
    # print("data", response_data)
    # response_data = json.loads(response_data)
    prof_id = DB.GET(
        f"""SELECT * FROM `description_profession` ORDER BY price_junior DESC""")
    req_data = []
    for i in prof_id:
        print(i)
        g = {
            "id": i[0],
            "title": i[1],
            "description": i[2],
            "time_learning": i[3],
            "price_junior": i[4]}
        req_data.append(g)
    mass_elem = {"elements": req_data}
    return mass_elem


@application.route('/api/0.1/get_circle_data', methods=["POST"])
def get_circle_data():
    response_data = request.data.decode()
    print(response_data)
    response_data = json.loads(response_data)
    if not "id" in response_data:
        abort(400)
    prof_micro_info = DB.GET(
        f"""SELECT * FROM `description_circle_python` WHERE id = {response_data["id"]}""")
    req_data = []
    i = prof_micro_info[0]
    url_url = DB.GET(
        f"""SELECT `url_name`, `url` FROM `url_for_users_to_learning` WHERE id_circle_name = {response_data["id"]}""")
    mass_elem = {
        "id": i[0],
        "name": i[1],
        "description": i[2],
        "theoryDuration": i[3],
        "practiceDuration": i[4],
        "src_img": i[5],
        "type_size": i[6],
        "type_profession": i[7],
        "url_to_page": "https://netology.ru/programs/python",
        "url_url": []
    }
    for i in url_url:
        mass_elem["url_url"].append({"url": i[1],
                                     "url_name": i[0]})

    # print(mass_elem)
    return mass_elem, 200


@application.route('/api/0.1/get_questions', methods=["POST"])
def get_questions():
    response_data = request.data.decode()
    print("data", response_data)
    response_data = json.loads(response_data)
    # if not "id" in response_data:
    #     abort(400)
    questions_info = DB.GET(
        f"""SELECT * FROM `questions` WHERE `profession` = '{response_data["profession"]}'""")
    req_data = []
    for i in questions_info:
        print(i)
        g = {
            "id": i[0],
            "profession": i[1],
            "question": i[2],
            "answer_1": i[3],
            "answer_2": i[4]}
        req_data.append(g)
    mass_elem = {"elements": req_data}
    return mass_elem, 200


@application.route('/api/0.1/get_progress_user', methods=["POST"])
def get_progress_user():
    response_data = request.data.decode()
    print("data", response_data)
    response_data = json.loads(response_data)
    get_progress_info = DB.GET(
        f"""SELECT * FROM `progress_user` WHERE `id` = '{response_data["id"]}'""")
    # print(get_progress_info)
    req_data = []
    i = get_progress_info[0]
    # print(i)
    g = {
        "id_user": i[1],
        "id_circle": i[2]
    }
    if response_data["append"] == "":
        g["type"] = i[3]
    else:
        print("asd")
        post_progress_info = DB.POST(
            f"""UPDATE `progress_user` SET `type`= '{response_data["append"]}' WHERE `id` = '{response_data["id"]}'""")
        g["type"] = response_data["append"]

    mass_elem = {"elements": g}
    return mass_elem, 200


@application.route('/api/0.1/questions_and_img', methods=["POST"])
def questions_and_img():
    response_data = request.data.decode()
    print("data", response_data)
    response_data = json.loads(response_data)
    questions_info = DB.GET(
        f"""SELECT * FROM `questions` WHERE `profession` = '{response_data["profession"]}'""")
    req_data = {
        "questions": []
    }
    for i in questions_info:
        print(i)
        g = {
            "question": i[2],
            "answers": [
                {
                    "answer": i[3],
                    "img": f"{i[0]}_1.jpg"
                },
                {
                    "answer": i[4],
                    "img": f"{i[0]}_2.jpg"
                }
            ]
        }
        req_data["questions"].append(g)
    mass_elem = {"elements": req_data}
    return mass_elem, 200


data_user = {
    'cc': {
        'access_tokin': '',
        'refresh_tokin': ''
    }
}


def get_user_data(hash):
    # Если нет пользователя то создаёт его
    if not hash in data_user:
        data_user[hash] = {
            'auth': False,
            "user_ip": "",
            'completed_learn': ''
        }
    return data_user[hash]


def generate_account_hash(IPs):
    cc = str('_AA_' + str(IPs) + '_AA_' + str(datetime.datetime.now()))
    # print(cc)
    bytesvalue = cc.encode('utf-8')
    hash_object = hashlib.md5(bytesvalue)
    Hash_user = (hash_object.hexdigest())
    # print(Hash_user)
    return(Hash_user)


@application.route('/api/0.1/user_login', methods=["POST"])
def user_login():
    response_data = request.data.decode()
    print("data", response_data)
    response_data = json.loads(response_data)
    account_hash = 0
    # print(hash)
    if not request.cookies.get('account_hash'):
        account_hash = generate_account_hash(request.remote_addr)
    else:
        account_hash = request.cookies.get('account_hash')
    now_user = get_user_data(account_hash)
    if now_user["auth"] == False:
        if not "login" in response_data or "password" not in response_data:
            abort(400)
        user_login = DB.GET(
            f"""SELECT * FROM `users` WHERE `login` = '{response_data["login"]}'""")
        if str(user_login) == "()":
            abort(400)
        if response_data["password"] != user_login[0][6]:
            abort(400)
        print(str(user_login))
        # data_user["data_auth"] =

        now_user["auth"] = True
        print(data_user)
        mass_elem = {"elements": "req_data"}
        res = make_response(mass_elem)
        res.set_cookie('account_hash', account_hash, 60*60*400)
        return res, 200
    else:
        abort(400)


# "95.172.70.131"
@application.errorhandler(400)
def error_400(e):
    return "Bad request", 400


# http://deadbf914c1c.ngrok.io
if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=4567)  #
