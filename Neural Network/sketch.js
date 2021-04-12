let training_data = [
    {
        inputs: [0,0],
        target: [0]    
    },
    {
        inputs: [1,0],
        target: [1]    
    },
    {
        inputs: [0,1],
        target: [1]    
    },
    {
        inputs: [1,1],
        target: [0]    
    },
]

function setup() {
    let nn = new NeuralNetwork(2, 2, 1)

    for (let i=0; i<100000; i++){
        let data = random(training_data)
        nn.train(data.inputs, data.target)
    }
    // let output = nn.feedforward(input)
    // console.log(output)
    console.log(nn.feedforward([0,0]))
    console.log(nn.feedforward([1,0]))
    console.log(nn.feedforward([0,1]))
    console.log(nn.feedforward([1,1]))
}

function draw() {}