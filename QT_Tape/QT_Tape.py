from Turing_machine import Turing_machine 
from Turing_machine_emulator import Turing_machine_emulator 
from Decoder import Decoder 
from Get_Machine import Get_Machine
from playsound import playsound
import pathlib
import time


# lineedit.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QAction, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QPixmap
from PyQt5 import QtCore

class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() # Initializer which calls constructor for QWidgself.initializeUI() # Call function used to set up window
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 1440, 1024) # x, y, width, height
        self.setWindowTitle('Turing Machine Simulator')
        self.createMenu()
        self.displayWidgets()
        self.displayToolbar()
        self.show()
    
    def createMenu(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)


    def displayToolbar(self):
        ####Run Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/run_button'
        run_button_icon = QIcon()
        run_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        run_button = QPushButton(self)
        run_button.clicked.connect(self.run_buttonClicked)
        run_button.resize(36, 36)
        run_button.move(22, 32)
        run_button.setIcon(run_button_icon)
        run_button.setIconSize(QSize(36,36))
        run_button.setStyleSheet("border: none;")
        #########

        ###Pause Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/pause_button'
        pause_button_icon = QIcon()
        pause_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        pause_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        pause_button.resize(14, 25)
        pause_button.move(96, 36)
        pause_button.setIcon(pause_button_icon)
        pause_button.setIconSize(QSize(14, 25))
        pause_button.setStyleSheet("border: none;")
        #########

        ####Stop Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/stop_button'
        stop_button_icon = QIcon()
        stop_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        stop_button = QPushButton(self)
        #stop_button.clicked.connect(self.run_buttonClicked)
        stop_button.resize(25, 25)
        stop_button.move(170, 36)
        stop_button.setIcon(stop_button_icon)
        stop_button.setIconSize(QSize(25, 25))
        stop_button.setStyleSheet("border: none;")
        #########

        ####Save Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/save_button'
        save_button_icon = QIcon()
        save_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        save_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        save_button.resize(25, 25)
        save_button.move(244, 36)
        save_button.setIcon(save_button_icon)
        save_button.setIconSize(QSize(25, 25))
        save_button.setStyleSheet("border: none;")
        #########
        
        ####Reset Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/reset_button'
        reset_button_icon = QIcon()
        reset_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        reset_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        reset_button.resize(25, 25)
        reset_button.move(318, 36)
        reset_button.setIcon(reset_button_icon)
        reset_button.setIconSize(QSize(25, 25))
        reset_button.setStyleSheet("border: none;")
        #########

    def displayWidgets(self):

        ####Pointer####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/pointer2'
        run_button_icon = QIcon()
        run_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        pointer = QLabel(self)
        pointer.resize(48,32)
        pixmap = QPixmap(path)        
        pointer.setPixmap(pixmap)
        pointer.move(696, 178)
        #########        

        ####Tape#####
        self.name_entry = list()
        
        ######Temp input########
        text = list()
        for i in range(0,10):
            text.append(' ')
        text.append('1')
        text.append('0')
        text.append('1')
        text.append('|')
        text.append('1')
        text.append('1')
        for i in range(15,27):
            text.append(' ')
        ###############

        for i in range(0,27):     
            self.name_entry.append(QLineEdit(self))
            self.name_entry[i].setAlignment(Qt.AlignLeft) # The default alignmeis AlignLeft
            self.name_entry[i].move(45+i*50, 95)
            self.name_entry[i].resize(46, 80) # Change size of entry field
            self.name_entry[i].setMaxLength(1)
            self.name_entry[i].setAlignment(QtCore.Qt.AlignCenter)
            self.name_entry[i].setStyleSheet("background-color:rgb(255,255,239); color:rgb(78,78,78);")
            self.name_entry[i].setFont(QFont("Roboto",60))
            self.name_entry[i].setText(text[i])
        

        
    def input_data(self, Emulator):
        for i in range(len(self.name_entry)):
            Emulator.tape[i-13] = self.name_entry[i].text()  

    def get_data(self, Emulator):
        for i in range(len(self.name_entry)):
            try:
                self.name_entry[i].setText(Emulator.tape[i-13+Emulator.position])
            except KeyError:
                self.name_entry[i].setText(' ')
                    
        
    def run_buttonClicked(self):
        Machine = Get_Machine()
        Emulator = Turing_machine_emulator()
        self.input_data(Emulator)
        print(Emulator.tape)
        print(Emulator.position)
        emulate = 1
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/sounds/test3.mp3'
        while (emulate == 1):
            emulate = Emulator.emulate_one_step(Machine)
            self.get_data(Emulator)
            QApplication.processEvents()
            #playsound(path)
            #time.sleep(0.005)
        QMessageBox().information(self, "Emulator", "Емулятор успішно закінчив свою роботу!", QMessageBox.Ok, QMessageBox.Ok)



# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

