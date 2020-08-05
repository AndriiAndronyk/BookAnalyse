from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import gui
import sys


class MainWindow(QMainWindow, gui.Ui_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.StartAnalyse)
        self.toolButton.clicked.connect(self.OutputWords)

    def StartAnalyse(self):
        print('There will be magically created with the help of a 🐼 and 🐍 ')

    def OutputWords(self):
        print('There will words for learning export func ')

    def CloseApp(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec()
