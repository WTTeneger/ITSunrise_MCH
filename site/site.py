from flask import Flask, render_template, request, session, Response, make_response, redirect, jsonify, abort
from flask_cors import CORS
import datetime
import uuid
import hashlib
import pymysql
import time
import string
import threading
import random
import json
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
    return render_template("index.html")


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
    print("data", response_data, len(response_data))
    response_data = json.loads(response_data)
    if not "id" in response_data:
        abort(400)
    prof_micro_info = DB.GET(
        f"""SELECT * FROM `description_circle` WHERE id = {response_data["id"]}""")
    req_data = []
    i = prof_micro_info[0]
    mass_elem = {
        "id": i[0],
        "name": i[1],
        "description": i[2],
        "learning_time": i[3],
        "type_size": i[4],
        "type_profession": i[5]}
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


# "95.172.70.131"
@application.errorhandler(400)
def error_400(e):
    return "Bad request", 400


# http://deadbf914c1c.ngrok.io
if __name__ == "__main__":
    application.run(debug=True,  port=4567)  # host="0.0.0.0",
