# Draw number and CNN predicts it
Application where user draws numbers and convolutional neural network predicts the number.
savedModels contains the current CNN model. The model had validation accuracy of 99.017 with 47 training epochs. Model contains convolutional layer (16 filters, 3x3 kernel), max pooling with 2x2 pool size, 2x convolutional layers (32 filter 3x3 kernel, 64 filter, 3x3 kernel), another max pooling with 2x2 pool size, flatten, 2 dense layers with 32 units and relu activation and finally dense layer with 10 units and softmax layer.

The training was done with the MNIST_Training.py.
The main program is in main.py and mnistapp.kv files.


The program starts when the user presses the "Start" button. Then the user can draw on the black area.
![start](https://github.com/Jarsse/NumberDrawingKivyMnist/blob/main/images/start.png?raw=true)
The "Reset" button removes the current drawings and predict button asks the neural network to predict which number is currently drawn. 
Currently the program also has 20% chance to give prediction each time the user draws something on the screen.
![two](https://github.com/Jarsse/NumberDrawingKivyMnist/blob/main/images/two.png?raw=true)
The network predicts the numbers pretty well.
![three](https://github.com/Jarsse/NumberDrawingKivyMnist/blob/main/images/three.png?raw=true)

![five](https://github.com/Jarsse/NumberDrawingKivyMnist/blob/main/images/five.png?raw=true)
Sometimes the network gives wrong answers but so far it has given the right prediction after more precise drawing or whitening the image with more clicks.
