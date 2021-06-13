

import json
import requests
from bs4 import BeautifulSoup
import pymysql
import time
headers = {"content-type": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279 (Edition Yx GX)"}

# https://netology.ru/programs/python#/lessons"
dev = {
    "Python": "programs%2Fpython",
    "1C": "programs%2Fdeveloper1c"
}
url = f"https://netology.ru/backend/api/page_contents/{dev['Python']}"
get_req = requests.get(url, headers=headers).json()
# print(get_req)
# soup = BeautifulSoup(get_req.get_req, 'lxml')
# print(soup)
# with open("hackathon\\ITSunrise_MCH\\parser\\netologiya_Python.json", "w", encoding='utf8') as file:
#     # json.dump(get_req.get_req, file)
#     file.write(json.dumps(get_req.get_req, sort_keys=True,
#                           indent=4, ensure_ascii=False))
#     file.close()

# time.sleep(100)
# with open("hackathon\\ITSunrise_MCH\\parser\\netologiya_Python.json", "r", encoding='utf8') as file:
#     get_req = json.load(file)
#     file.close()


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

# Основы языка программирования Python


programModule = [str(i) for i in get_req["content"].keys()
                 if "programModule" in i][0]

i_for_img = 0
for i in get_req["content"][programModule]["blocks"]:
    # print(i["title"])
    support = i["title"].replace(
        "<p>", "").replace("</p>", "").replace("<br />", "")
    support_description = i["description"].replace("<p>", "").replace(
        "</p>", "").replace("&nbsp;", "").replace("&laquo;", "").replace("&raquo;", "")
    theoryDuration = i["theoryDuration"].replace(
        "<p>", "").replace("</p>", "")
    practiceDuration = i["practiceDuration"].replace(
        "<p>", "").replace("</p>", "")

    print(support)
    print(support_description)
    print(theoryDuration)
    print(practiceDuration)
    if i_for_img != 0:
        try:
            logo = get_req["content"]["resume"]["technologies"][i_for_img]["icon"]
            print(logo)
            i_for_img += 1
        except:
            print("i", i)
            print("None")
    print("_"*60)
    # post_to_DB = DB.POST(f"""INSERT INTO `description_circle`\
    # (`name`, `description`, `theoryDuration`, `practiceDuration`, `src_img`, `type_size`, `type_profession`) \
    #     VALUES ('{support}','{support_description}','{theoryDuration}','{practiceDuration}', '{logo}', 1, 1)""")
