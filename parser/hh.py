
import json
import requests
from bs4 import BeautifulSoup

url = "https://api.hh.ru/"
headers = {"content-type": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.279 (Edition Yx GX)"}
# ,  # Текст фильтра. В имени должно быть слово "Аналитик"

# req_get = requests.get('https://api.hh.ru/vacancies',
#                        data=data, headers=headers)  # Посылаем запрос к API

# req_get.close()
num_vacancies = 0
mass_price = []


def parse(page):
    data = {'text': 'C++',
            'area': 1,  # Поиск ощуществляется по вакансиям города Москва
            'page': page,  # Индекс страницы поиска на HH
            'per_page': '100'  # Кол-во вакансий на 1 странице
            }
    req_get = requests.get("https://api.hh.ru/vacancies", data)
    # Декодируем его ответ, чтобы Кириллица отображалась корректно
    global req_get_dec
    req_get_dec = req_get.json()
    # print(req_get_dec)

    for i in req_get_dec["items"]:
        # print(i["name"])

        global num_vacancies
        num_vacancies += 1
        if i["salary"] != None and i["salary"]["from"] != None \
                and i["salary"]["currency"] == "RUR":
            # print(i["salary"]["currency"],
            #       "От:", i["salary"]["from"],
            #       "До:", i["salary"]["to"])

            mass_price.append(i["salary"]["from"])
        else:
            pass
            # print("_Не указанна_")


for i in range(1, 20):
    if i == 19:
        print(req_get_dec)
    try:
        parse(i)
    except:
        print("qwe")
        print(req_get_dec)
        break
    print(i)
# print(sum(mass_price),len(mass_price))
print(mass_price)
sel = sum(mass_price)/len(mass_price)
print(int(sel))
print(num_vacancies)


with open("hackaton\\file_api.txt", "w", encoding='utf8') as file:
    file.write(json.dumps(req_get_dec, sort_keys=True,
                          indent=4, ensure_ascii=False))
    file.close()
