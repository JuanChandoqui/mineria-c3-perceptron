import sys
from Controllers.home_controller import HomeController
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    homeApp = HomeController()
    homeApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')