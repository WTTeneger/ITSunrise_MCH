from flask import Flask, render_template, request, session, Response, make_response, redirect, jsonify
from flask_cors import CORS
import datetime
import uuid
import hashlib
import sqlite3
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
        connection = pymysql.connect(host="37.140.192.90", user='u1102095_ting',
                                     password='S7x6U9j2', database='u1102095_tg_bot', charset="utf8mb4")
        cursor = connection.cursor()
        cursor.execute(self)
        OTV = cursor.fetchall()
        return(OTV)

    def POST(self):
        """Отправляет данные в Базу данных
        """
        connection = pymysql.connect(host="37.140.192.90", user='u1102095_ting',
                                     password='S7x6U9j2', database='u1102095_tg_bot', charset="utf8")
        cursor = connection.cursor()
        cursor.execute(self)
        connection.commit()
        return('True')


@application.route('/')
def index():
    # Вывод страницы
    return render_template("index.html")


@application.route('/num', methods=["GET", "POST"])
def num_print():
    # response_data = request.data.decode()
    # response_data = json.loads(response_data)
    # print(response_data["null"])
    response_data = {"qwe": "qwe"}
    response_data["status"] = "none"
    # json.loads(per)

    return response_data
    # name+" " + str(num)


if __name__ == "__main__":
    application.run(debug=True)
