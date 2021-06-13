import numpy as np
 
 
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
 
 
training_inputs = np.array([[1, 1, 0],
                            [1, 0, 0],
                            [0, 1, 0],
                            [0, 1, 1]])
 
training_outputs = np.array([[0.00, 0.01, 0.02, 0.03]]).T
 
np.random.seed(1)
 
synaptic_weights = 2 * np.random.random((3, 1)) - 1
print("Случайные веса: ")
print(synaptic_weights)
 
# Метод обратного распространени
for i in range(70000):
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