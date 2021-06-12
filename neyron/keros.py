#!/usr/bin/python3
#-*- coding: utf-8 -*-


from keras.models import Sequential
from keras.layers.core import Dense
import tensorflow as tf
import keras
import numpy as np # для массивов.


x_train = np.array([
[1, 1, 1, 2, 2, 2, 2, 2], # Тестеровщик по 0.01
[1, 1, 2, 2, 1, 2, 1, 2], # Инженер по тестированию 0.02
[1, 1, 2, 2, 1, 2, 2, 2], # java  0.03
[1, 1, 2, 1, 1, 1, 2, 2], # java  0.04
]) # можно бесконечно много дополнять.




# 0.1- первая, 0.2 - вторая и тд.
# .T - транспонирует массив (матрицу).

y_train =  np.array([1, 2, 3, 3])
# y_train =  np.array([0.1, 0.2, 0.3, 0.3])




model = Sequential()
model.add(Dense(8, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='relu'))

# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
# history = model.fit(x_train, y_train, epochs=5, batch_size=32)
h = model.fit(x_train, y_train, epochs=500, batch_size=10)
# print(h.history)
# loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
# print(loss_and_metrics)


scores = model.evaluate(x_train, y_train)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# print(history.history)

x_test = np.array([
[1, 1, 2, 1, 1, 1, 2, 2]])
classes = model.predict(x_test, batch_size=128)
print(classes)
x_test = np.array([
[1, 1, 2, 2, 1, 2, 1, 2]])
classes = model.predict(x_test, batch_size=128)
print(classes)