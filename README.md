# NumberDrawingKivyMnist
Application where user draws numbers and convolutional neural network predicts the number.
savedModels contains the current CNN model. The model had validation accuracy of 99.017 with 47 training epochs. Model contains convolutional layer (16 filters, 3x3 kernel), max pooling with 2x2 pool size, 2x convolutional layers (32 filter 3x3 kernel, 64 filter, 3x3 kernel), another max pooling with 2x2 pool size, flatten, 2 dense layers with 32 units and relu activation and finally dense layer with 10 units and softmax layer.

The training was donr with the MNIST_Training.py.
The main program is in main.py and mnistapp.kv files.

