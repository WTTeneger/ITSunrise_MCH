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
[1, 1, 1, 2, 2, 2, 2, 2], # Тестеровщик по 0.01
[1, 1, 2, 2, 1, 2, 1, 2], # Инженер по тестированию 0.02
[1, 1, 2, 2, 1, 2, 2, 2], # java  0.03
[1, 2, 2, 2, 1, 2, 2, 2], # Чистый бэк python 0.04
[1, 1, 1, 1, 1, 1, 2, 1], # Game def 0.05
[1, 1, 2, 1, 2, 1, 2, 2], # 1C программист 0.06
[1, 2, 2, 2, 2, 1, 2, 2], # Системный админ 0.07
[1, 1, 1, 1, 1, 1, 1, 2], # Любой фулл стак 0.08 python
[1, 2, 1, 1, 1, 2, 1, 2], # Веб разраб 0.09
[1, 2, 1, 1, 1, 1, 1, 2], # Фул стак 0.14
[1, 2, 1, 2, 2, 1, 1, 2], # Bitrix 0.15
]) # можно бесконечно много дополнять.



qe = []
for el in range(len(inputs)):
  # print(el)
  qe.append(el * (1/len(inputs)))

# 0.1- первая, 0.2 - вторая и тд.
# .T - транспонирует массив (матрицу).
rs =  [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.14, 0.15]
results = np.array([ # правильные результаты.
  qe
]).T 


"""
  Отмечу, что взяты пропорции знаменитостей (взрослые люди).
  У детей и подростков другое соотношение, поэтому для них
  сеть даёт неправильный результат, хотя можно обучить.
"""

model = Perceptron(inputs) # создаем экземпляр класса.
q = model.training(results, 500000, mse_print = True) # тренируем модель.
print('Веса', q)
"""
  Даём новые данные и скармливаем сетке:
"""

#1, 2, 1, 2, 1, 1, 1, 2
new_inputs = np.array([1, 1, 1, 2, 2, 2, 2, 2]) # пустые данные
result = model.prediction(new_inputs, q) # предсказание на новые данные.

print('result1', result["result_1"])


new_inputs = np.array([1, 2, 1, 1, 1, 1, 1, 2]) # пустые данные 14
result = model.prediction(new_inputs, q) # предсказание на новые данные.

print('result2', result["result_1"])

print(qe)
# a = min(rs, key=lambda x: abs(result["result_1"]-x))

# tasks = ''
# with open('F:\\1py\\hackathon\\neyron\\only_dev.json', encoding='utf-8') as f:
#     tasks = json.load(f)


# task = findEl(a, 'weight', tasks)


# print("\nНовые данные:", result["inputs"])
# print("Ответ модели:", a, "\n")
# print("Данные на какую профессию:", task['name'], "\n")