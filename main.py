import numpy as np
from tensorflow.keras.models import load_model
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class DrawingScreen(Widget):
    buttons = []
    created_model = False

    def build(self):
        for i in range(self.ids.Grid.cols):
            self.buttons.append([])
            for j in range(self.ids.Grid.rows):
                btn = Button(text=" ", size_hint=(0.01, 0.01), on_press=lambda btn:self.change_color(btn), background_color=(0, 0, 0, 1))
                self.ids.Grid.add_widget(btn)
                self.buttons[i].append(btn)
        print("Finished!")


    def change_color(self, button):
        """
        Changes the color of the button between black and white.
        :param button: button which color will be changed
        """
        if button.background_color[0] < 1:
            button.background_color = (1., 1., 1., 1)
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                if button == self.buttons[i][j]:
                    neighbours = self.getNeighbours(i, j)
                    for btn in neighbours:
                        for z in range(3):
                            btn.background_color[z] += 1.

        # auto predict with ~20% chance each time user draws
        rand = np.random.rand()
        if rand < .2:
            self.predict()

    def getNeighbours(self, i, j):
        """
        Get direct neighbours to the button at location [i][j].
        :param i: row location of the button
        :param j: column location j of the button
        :return: List of neighbouring buttons
        """
        neighbours = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if i+y >= 0 and i+y <= len(self.buttons)-1 and j+x >= 0 and j+x <= len(self.buttons[i])-1:
                    neighbours.append(self.buttons[i+y][j+x])
        return neighbours

    def start_button(self, button):
        """
        Starts the program. Changes button text from Start to Reset and
        generates the drawing field with self.build()
        :param button: Start button
        """
        button.text = "Reset"
        self.build()

    def reset_button(self):
        """
        Resets the drawing field back to its original color.
        """
        print("Reset")
        self.ids.Prediction1.text = "Prediction: "
        for i in range(len(self.buttons)):
            for j in range(len(self.buttons[i])):
                self.buttons[i][j].background_color = (0, 0, 0, 1)

    def predict(self):
        """
        Predicts which number the user drew if Start-button has been pressed earlier.
        Gets the data from the UI, preprocesses it and predicts the number.
        """
        if self.ids.Start.text == "Reset":
            print("Predicting..")
            data = []
            for i in range(len(self.buttons)):
                for j in range(len(self.buttons[i])):
                    data.append(self.buttons[i][j].background_color[0])
            data = self.predict_preprocess(data)
            pred1 = self.predict_model(data)
            self.ids.Prediction1.text = "Prediction: {}".format(pred1)
        else:
            print("Start first")

    def predict_preprocess(self, data):
        """
        Preprocess the data to right type and shape for the neural network.
        :param data: Data to be preprocessed
        :return: Preprocessed data
        """
        data = np.asarray(data)
        data = data.astype("float32")
        data = data.reshape(-1, 28, 28, 1)
        return data

    def predict_model(self, data):
        """
        On the first prediction, load the trained model for MNIST prediction.
        Then, get the prediction from the model.
        :param data: The user's drawing of a number
        :return: The prediction.
        """
        if not self.created_model:
            self.model1 = load_model("savedModels/mnist_model_5")
            self.created_model = True
        prediction1 = self.model1.predict_classes(data)
        return prediction1


class MnistApp(App):
    def build(self):
        return DrawingScreen()


if __name__ == "__main__":
    MnistApp().run()
