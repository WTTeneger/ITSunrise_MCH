var myNetwork = new synaptic.Architect.Perceptron(3, 2, 1)

var trainer = new synaptic.Trainer(myNetwork)

var trainingSet = [{
    input: [1, 1, 1, 0, 0, 0, 0, 0],
    output: [0]
}, {
    input: [1, 1, 0, 0, 1, 0, 1, 0],
    output: [0.01]
}, {
    input: [1, 1, 0, 0, 1, 0, 0, 0],
    output: [0.02]
}, {
    input: [1, 1, 0, 1, 1, 1, 0, 0],
    output: [0.03]
}]

var trainingOptions = {
    rate: .1,
    iterations: 2000000,
    error: .000005,
}

console.log(trainer.train(trainingSet, trainingOptions));

// console.log(myNetwork.activate([0, 0, 1]));
// console.log(myNetwork.activate([1, 0, 0]));
// console.log(myNetwork.activate([1, 1, 1]));

console.log(myNetwork.activate([1, 1, 1, 0, 0, 0, 0, 0]));
console.log(myNetwork.activate([1, 1, 0, 0, 1, 0, 0, 0]));
console.log(myNetwork.activate([1, 1, 0, 1, 1, 1, 0, 0]));