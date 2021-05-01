from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QLabel)
import sys

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 200, 1000, 500) # x, y, width, height
        self.setMinimumSize(1000, 500)
        self.setWindowTitle('Turing Machine Simulator')
        self.createMenu()
        self.displayLabels()
        self.show()

    def createMenu(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)

    def displayLabels(self):
        text = QLabel(self)
        text.setText("Hello")
        text.move(500, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
