from mainwindow import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer, QDateTime, QEventLoop


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("打字快一點！")
        
        self.pushButton.clicked.connect(self.buttonClicked)
        self.textEdit.textChanged.connect(self.checkTyping)
    
        self.timer = QTimer(self)
        self.count = 5
        self.timer.timeout.connect(self.showNum)
        self.timer.start(1000)
        self.startCount()
        
    def buttonClicked(self):
        self.textEdit.clear()
    
    def checkTyping(self):
        self.count = 5
    
    def showNum(self):
        self.count = self.count - 1
        print(self.count)
        if self.count == 0:
            self.textEdit.clear()
    
    def startCount(self):
        self.timer.start(1000)


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())