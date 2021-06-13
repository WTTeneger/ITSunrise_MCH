import json
import requests
from bs4 import BeautifulSoup
import pymysql
import time
headers = {"content-type": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279 (Edition Yx GX)"}


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


all_theme = DB.GET(
    f"""SELECT `id`, `name` FROM `description_circle_python`""")
print(all_theme)
mass_url = []
for i in all_theme:
    id_ = i[0]
    title = i[1].replace(" ", "+")
    print(id_, title)
    url = f"https://www.google.ru/search?q={title}"

# time.sleep(100)
    get_req = requests.get(url, headers=headers)  # .json()
# print(get_req.content)  #
# with open("hackathon\\ITSunrise_MCH\\parser\\google.txt", "w", encoding='utf8') as file:
#     # json.dump(get_req.get_req, file) kCrYT
#     file.write(get_req.text)
#     file.close()
    soup = BeautifulSoup(get_req.content, 'html.parser')
    text = soup.find_all('div', attrs={'class': 'kCrYT'})
# print(text[3].a["href"].split("&")[0].replace("/url?q=", ""))
    mass_url_ = []
    # id_ = 0
    for i in text:
        if len(mass_url_) >= 3:
            mass_url += mass_url_
            break
        else:
            # id_ += 1
            try:
                if "wikipedia" in i.a["href"].split("&")[0].replace("/url?q=", "") or "Картинки" in i.div.text:
                    break
                # print()
                url = i.a["href"].split("&")[0].replace("/url?q=", "")
                url_text = i.div.text

                mass_url_.append(i.a["href"].split(
                    "&")[0].replace("/url?q=", ""))

                url_post = DB.POST(f"""INSERT INTO `url_for_users_to_learning`(`id_circle_name`, `url_name`, `url`) \
                    VALUES ({id_}, '{url_text}', '{url}')""")
            except:
                print("ошибка")
                # print(i)

    # print("_"*80)
# text = text.
print(mass_url)
