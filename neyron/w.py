#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys # для импорта модели.
import json
from model import Perceptron # модель.

import numpy as np # для массивов.
import os, warnings


def findEl(find_el, Field, json):
    """Поиск элемента в json

    Args:
        el: Зачение которое ищем
        Field ([type]): В каком столбце ищем
        json ([type]): json файл
    """    

    for el in json:
        if(str(Field) in el):
            if str(el[Field]) == str(find_el):
                return(el)
                break






warnings.filterwarnings("ignore") # отключаем warnings.
# os.system("clear") # очищаем терминал.

"""
  Сделаем так, чтобы наша сеть умела предсказывать пол
  человека по его росту, весу и возрасту.
  x1. x2. x3. x - ответ на вопрос N
"""
# данные
inputs = np.array([
    [2, 2, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1],  # Тестеровщик по 0.01
    [2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1],  # Инженер по тестированию 0.02
    [2, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 1],  # Java-разработчик с нуля 0.03
    [1, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1],  # Чистый бэк python 0.04
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Game def 0.05
    [2, 2, 1, 2, 1, 2, 2, 1, 2, 2, 2, 1],  # 1C программист 0.06
    [2, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1],  # Системный админ 0.07
    [1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1],  # Fullstack-разработчик на Python 0.08
    [1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 1],  # Веб-разработчик с нуля 0.09
    [1, 2, 1, 2, 2, 1, 2, 1, 2, 2, 2, 1],  # Специалист по информационной безопасности с нуля 0.10
    [2, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 1],  # Android-разработчик с нуля 0.11
    [1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1],  # Frontend-разработчик с нуля 0.12
    [2, 1, 1, 1, 1, 2, 1, 2, 2, 1, 1, 1],  # iOS-разработчик с нуля 0.13
    [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 2, 1],  # Fullstack-разработчик на JavaScript 0.14
    [2, 2, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1],  # Bitrix 0.15
]) # можно бесконечно много дополнять.

# 0.1- первая, 0.2 - вторая и тд.
# .T - транспонирует массив (матрицу).

qe = []
for el in range(len(inputs)):
  # print(el)
  el += 1
  qe.append(el * 1/len(inputs[0]))
# rs = 
# print(qe)
rs =  qe#, 0.11, 0.12, 0.13, 0.14, 0.15]

results = np.array([ # правильные результаты.
  qe
]).T 


"""
  Отмечу, что взяты пропорции знаменитостей (взрослые люди).
  У детей и подростков другое соотношение, поэтому для них
  сеть даёт неправильный результат, хотя можно обучить.
"""

model = Perceptron(inputs) # создаем экземпляр класса.
q = model.training(results, 1000000, mse_print = False) # тренируем модель.
print('Веса', q)
"""
  Даём новые данные и скармливаем сетке:
"""

#1, 2, 1, 2, 1, 1, 1, 2
new_inputs = np.array([2, 2, 1, 2, 2, 1, 2, 1, 1, 1, 2, 1]) # пустые данные
result = model.prediction(new_inputs, q) # предсказание на новые данные.

print(result)

print("Ответ модели:", result, "\n")
a = min(rs, key=lambda x: abs(result["result_1"]-x))
print(a)


# tasks = ''
# with open('F:\\1py\\hackathon\\neyron\\only_dev.json', encoding='utf-8') as f:
#     tasks = json.load(f)

# task = findEl(a, 'weight', tasks)
# print("\nНовые данные:", result["inputs"])

# print("Данные на какую профессию:", task['name'], "\n")