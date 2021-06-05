from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
import sys
 
def display():
    print(text_edit.toPlainText())
 
app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(400,400,300,300)
window.setWindowTitle("CodersLegacy")
 
text_edit = QtWidgets.QTextEdit(window)
text_edit.setPlaceholderText("Enter some text here")
 
button = QtWidgets.QPushButton(window)
button.setText("Press me")
button.clicked.connect(display)
button.move(100,200)
 
window.show()
sys.exit(app.exec_())
