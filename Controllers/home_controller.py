from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from Functions.perceptron import perceptron_main

from Views.Ui_home_view import Ui_MainWindow

class HomeController(QMainWindow):
    def __init__(self):
        super(HomeController, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_ejecutar.clicked.connect(self.executeAlgoritm)

    def executeAlgoritm(self):
        w0 = self.getWeights()
        result = perceptron_main(w0)
        self.ui.label_flowerType.setText(result)
        
        
    def getWeights(self):
        w0 = [1]
        #get values from spinBox (UI)
        for i in range(4):
            spinBox = getattr(self.ui,f'spinBox_w0_{i}').value()
            w = round(float(spinBox), 4)
            w0.append(w)

        return w0