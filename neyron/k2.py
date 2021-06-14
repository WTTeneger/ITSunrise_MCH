import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# training_inputs = np.array([[1, 1, 0],
#                             [1, 0, 0],
#                             [0, 1, 0],
#                             [0, 1, 1]])

# training_outputs = np.array([[0.00, 0.01, 0.02, 0.03]]).T
training_inputs = np.array([   # Последнее надо бы изменить
    #  0, 1,  4, 5, 6, 7, 8, 9, 10,11, 1, 1
    [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],  # Тестеровщик по 0.01
    [0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1],  # Инженер по тестированию 0.02
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],  # Java-разработчик с нуля 0.03
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],  # Чистый бэк python 0.04
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # Game def 0.05
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 1C программист 0.06
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Системный админ 0.07
    # Fullstack-разработчик на Python 0.08
    [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0],  # Веб-разработчик с нуля 0.09
    # Специалист по информационной безопасности с нуля 0.10
    [1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1],  # Android-разработчик с нуля 0.11
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],  # Frontend-разработчик с нуля 0.12
    [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],  # iOS-разработчик с нуля 0.13
    # Fullstack-разработчик на JavaScript 0.14
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0],  # Bitrix 0.15
])  # можно бесконечно много дополнять.

# 0.1- первая, 0.2 - вторая и тд.
# .T - транспонирует массив (матрицу).
rs = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07,
      0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
training_outputs = np.array([  # правильные результаты.
    rs
]).T
np.random.seed(1)

synaptic_weights = 2 * np.random.random((12, 1)) - 1
print("Случайные веса: ")
print(synaptic_weights)

# Метод обратного распространени
for i in range(170000):
    input_layer = training_inputs

    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    if i == 1:
        print(outputs)
    err = training_outputs - outputs

    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    synaptic_weights += adjustments

print("Веса после обучения: ")
print(synaptic_weights)

print("Результат после обучения: ")
for out in outputs:
    print(float(out), round(float(out) * 100))
