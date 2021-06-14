#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
  Импортируем numpy для математических вычислений.
  В коде будем использовать как np (as np).
"""
import numpy as np


"""
  Активационная функция - сигмоид:
  np.exp() - e, или число Эйлера - экспонента.
  В данном случае возведена в квадрат от -x.
  Если derivative равна True, то возвращает производную от функции.
"""


def sigmoid(x, derivative=False):
    if(derivative == True):
        return sigmoid(x) * (1 - sigmoid(x))  # производная.
    return 1 / (1 + np.exp(-x))


"""
  Класс одного нейрона:
"""


class Neuron(object):  # object необязательно писать.
    """
      Конструктор принимает в себя массив входных
      данных (inputs: x1, x2, ...) и bias - отклонение,
      по умолчанию = 0.
    """

    def __init__(self, inputs=None, bias=0):
        self.inputs = inputs
        self.bias = bias

    """
      Метод feedforward() - прямое распространение.
      Принимает в себя массив весов (weights: w1, w2, ...).
    """

    def feedforward(self, weights):
        """
          np.dot() - скалярное произведение. Вычисляется
          скалярное произведение inputs (входные данные
          полученные из конструктора) и weights (веса).
          Прибавляется отклонение (bias из конструктора).
          result = x1 * w1 + x2 * w2 + ... + bias
        """
        result = np.dot(self.inputs, weights) + self.bias
        """
          Результат проходит через нашу активационную функцию:
        """
        return sigmoid(result)
        """
          На выходе получается число в диапазоне от 0 до 1.
          Можно понимать как компрессию:
          1. Крупные отрицательные числа становятся ~ 0.
          2. Крупные положительные числа становятся ~ 1.
        """


"""
  Сам класс перцептрона:
"""


class Perceptron(object):
    def __init__(self, inputs=None, bias=0):
        """
          Инициализация одного нейрона и весов. Размерность массива весов
          одинакова с входными данными. Средний вес равен нулю.
        """
        self.x1 = Neuron(inputs, bias)
        self.inputs = inputs
        # если входные данные заданы, то инициализируются веса.
        if(inputs is not None):
            self.weights = 2 * np.random.random([len(inputs[0]), 1]) - 1

    """
      Среднеквадратичное отклонение (MSE):
      Используется для оценки качества тренировки сети.
      np.mean() - вычисляет среднее арифметическое.
      x - предполагаемые данные. y - правильные данные.
    """

    def mse(self, x, y):
        return np.mean((x - y) ** 2)

    """
      Метод тренировки сети возвращает оптимизированные веса.
      correct_results - правильные результаты для обучения модели.
      epochs - колличество итераций для цикла.
      learning_rate - скорость обучения сети, по умолчанию не задана.
      mse_print - по умолчанию выводит оценку обучения сети.
    """

    def training(self, correct_results, epochs=1000, learning_rate=None, mse_print=True):
        # Обучить сеть - это подобрать оптимальные веса.
        for epoch in range(epochs):
            """
              output - предсказание нейрона на основе весов.
              error - вычисление величины ошибки сети.
              delta - взвешивание производной сигмоиды с ошибкой.
              mse_value - оценка обучения сети (точность).
            """
            output = self.x1.feedforward(self.weights)
            error = correct_results - output
            delta = error * sigmoid(output, True)
            if(learning_rate):
                delta *= learning_rate
            self.weights += np.dot(self.inputs.T, delta)  # обновление весов.
            # оценка обучения.
            mse_value = self.mse(
                sigmoid(np.dot(self.inputs, self.weights)), correct_results)
            if(mse_print == True and epoch % 10 == 0):
                print("Эпоха:", str(epoch) + ", ошибка:", mse_value)
        return self.weights

    """
      Метод предсказания модели (возвращает словарь):
    """

    def prediction(self, inputs, weights=None):
        if(weights is None):
            # если веса не заданы, то используются веса модели.
            weights = self.weights
        prediction_1 = sigmoid(np.dot(inputs, weights))  # десятичный ответ.
        prediction_2 = round(float(prediction_1))  # округленный ответ.
        return {
            "inputs": str(list(inputs)).replace("[", "").replace("]", ""),
            "weights": str(weights).replace("[[", "[").replace("]]", "]"),
            "result_1": prediction_1[0],
            "result_2": prediction_2
        }
