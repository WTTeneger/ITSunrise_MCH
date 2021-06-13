import json
url_url = (('Основы программирования | Python 3 для начинающих ', 'https://pythonworld.ru/osnovy'),
           ('Введение в язык программирования Python 3. ... Быс',
            'https://pythonworld.ru/osnovy/tasks.html'),
           ('Самоучитель Python | Python 3 для начинающих и чай', 'https://pythonworld.ru/samouchitel-python'))
# print(dict(url_url[0]))
mass_elem = {
    "id":  [0],
    "name":  [1],
    "description":  [2],
    "theoryDuration":  [3],
    "practiceDuration":  [4],
    "src_img":  [5],
    "type_size":  [6],
    "type_profession":  [7],
    "url_to_page": "https://netology.ru/programs/python",
    "url_url": [{"qwe": ""}]
}
mass_elem["url_url"][0]["qwe"] = (url_url)
print(mass_elem)
