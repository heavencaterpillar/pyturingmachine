from Turing_machine import Turing_machine 
from Turing_machine_emulator import Turing_machine_emulator 
from Decoder import Decoder 
from Get_Machine import Get_Machine 
from playsound import playsound
import pathlib
import time
import copy


# lineedit.py
# Import necessary modules
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QAction, QLabel, QLineEdit, QPushButton, QMessageBox, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5.Qt import QTransform


class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() # Initializer which calls constructor for QWidgself.initializeUI() # Call function used to set up window
        self.initializeUI()
        self.reset_button
        self.run_button
        self.run_activated = False
        self.run_speed = 0
        self.emulator = Turing_machine_emulator() 
        self.saved_tape = copy.copy(self.emulator.tape)
        self.saved_position = copy.copy(self.emulator.position)



    def initializeUI(self):
        self.setGeometry(100, 100, 1440, 1024) # x, y, width, y_coord
        self.setWindowTitle('Turing Machine Simulator')
        self.displayPanels()
        self.createMenu()
        self.displayTape()
        self.displayToolbar()
        self.displayUndertape_panel()
        self.show()
    
    def displayPanels(self):
        ###Toolbar panel####
        Toolbar = QLabel(self)
        Toolbar.resize(1440, 79)
        Toolbar.move(0,0)
        Toolbar.setStyleSheet("background-color:rgb(54,54,54);")
        ############

        ###Tape panel####
        Tape = QLabel(self)
        Tape.resize(1440, 152)
        Tape.move(0,60)
        Tape.setStyleSheet("background-color:rgb(49,54,59);") # 39, 41, 45);")
        ############

        ###Undertape panel####
        Undertape = QLabel(self)
        Undertape.resize(1440, 40)
        Undertape.move(0,210)
        Undertape.setStyleSheet("background-color:rgb(37,37,38);")
        ############   



    def createMenu(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)
        menu_bar = self.menuBar()
        #menu_bar.resize(90,50)
        #menu_bar.setMaximumWidth(30)

        menu_bar.setNativeMenuBar(False)
        menu_bar.setStyleSheet("""
        QMenuBar {
            background-color: rgb(54,54,54);
            color: rgb(255,156,255);
            border: none;
        }

        QMenuBar::item {
            background-color: rgb(49,49,49);
            color: rgb(255,156,255);
        }

        QMenuBar::item::selected {
            background-color: rgb(45,45,45);
        }

        QMenu {
            background-color: rgb(49,49,49);
            color: rgb(255,156,255);         
        }

        QMenu::item::selected {
            background-color: rgb(45,45,45);
        }
        """)

        menu_font = QFont("Helvetica [Cronyx]", 10)
        menu_font.setStretch(200)
        menu_bar.setFont(menu_font)
        menu_bar.adjustSize()
        file_menu = menu_bar.addMenu('File')
        Run_menu = menu_bar.addMenu('Run')
        
        file_menu.addAction(exit_act)


    def displayToolbar(self):
        y_coord = 25 
        ####Run Button####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/run_button4'
        run_button_icon = QIcon()
        run_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        run_button = QPushButton(self)
        run_button.clicked.connect(self.run_buttonClicked)
        run_button.resize(74, 36)
        run_button.move(0, y_coord)
        run_button.setIcon(run_button_icon)
        run_button.setIconSize(QSize(31, 25))
        run_button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(50,50,50)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        self.run_button = run_button
        #########

        ###Pause Button####
        path = current_directory + '/icons/pause_button_activated'
        pause_button_icon = QIcon()
        pause_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        pause_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        pause_button.resize(74, 36)
        pause_button.move(74, y_coord)
        pause_button.setIcon(pause_button_icon)
        pause_button.setIconSize(QSize(14, 25))
        pause_button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(50,50,50)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        self.pause_button = pause_button
        #########

        ####Stop Button####
        path = current_directory + '/icons/stop_button2_activated'
        stop_button_icon = QIcon()
        stop_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        
        stop_button = QPushButton(self)
        #stop_button.clicked.connect(self.run_buttonClicked)
        stop_button.resize(74, 36)
        stop_button.move(148, y_coord)
        stop_button.setIcon(stop_button_icon)
        stop_button.setIconSize(QSize(25, 25))
        stop_button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(50,50,50)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        #########

        ####Save Button####
        path = current_directory + '/icons/save_button_activated'
        save_button_icon = QIcon()
        save_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        save_button = QPushButton(self)
        #run_button.clicked.connect(self.run_buttonClicked)
        save_button.resize(74, 36)
        save_button.move(222, y_coord)
        save_button.setIcon(save_button_icon)
        save_button.setIconSize(QSize(25, 25))
        save_button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(50,50,50)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        #########
        
        ####Reset Button####
        path = current_directory + '/icons/reset_button_activated'
        reset_button_icon = QIcon()
        reset_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        reset_button = QPushButton(self)
        reset_button.clicked.connect(self.reset_buttonClicked)
        reset_button.resize(74, 36)
        reset_button.move(296, y_coord)
        reset_button.setIcon(reset_button_icon)
        reset_button.setIconSize(QSize(25, 25))
        reset_button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(50,50,50)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        path = current_directory + '/icons/save_button'
        self.reset_button = reset_button
        #########

    def displayTape(self):

        ####Pointer####
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/pointer4'
        run_button_icon = QIcon()
        run_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        pointer = QLabel(self)
        pointer.resize(48,32)
        pixmap = QPixmap(path)        
        pointer.setPixmap(pixmap)
        pointer.move(694, 179)
        ######### 
         
        ####Left Button####
        path = current_directory + '/icons/left_button2_activated'
        left_button_icon = QIcon()
        left_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        left_button = QPushButton(self)
        left_button.clicked.connect(self.left_buttonClicked)
        left_button.resize(45, 80)
        left_button.move(0, 95)
        left_button.setIcon(left_button_icon)
        left_button.setIconSize(QSize(20, 80))
        left_button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(45,50,55);
                                }
                        
                                QPushButton {
                                    border: none;
                                    text-align:center;
                                }
                                """) # rgb(49,54,59)
        self.left_button = left_button
        #########     
         
        ####Right Button####
        path = current_directory + '/icons/right_button2_activated'
        right_button_icon = QIcon()
        right_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        right_button = QPushButton(self)
        right_button.clicked.connect(self.right_buttonClicked)
        right_button.resize(45, 80)
        right_button.move(1395, 95)
        right_button.setIcon(right_button_icon)
        right_button.setIconSize(QSize(20, 80))
        right_button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(45,50,55)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        self.right_button = right_button
        #########      

        ####Tape#####
        self.name_entry = list()

        for i in range(0,27):     
            self.name_entry.append(QLineEdit(self))
            self.name_entry[i].setAlignment(Qt.AlignLeft) # The default alignmeis AlignLeft
            self.name_entry[i].move(45+i*50, 95)
            self.name_entry[i].resize(46, 80) # Change size of entry field
            self.name_entry[i].setMaxLength(1)
            self.name_entry[i].setAlignment(QtCore.Qt.AlignCenter)
            self.name_entry[i].setStyleSheet("background-color:rgb(255,255,239); color:rgb(78,78,78);")
            self.name_entry[i].setFont(QFont("Roboto",50))
            self.name_entry[i].setText('')
            
    def displayUndertape_panel(self):
        return     

        
    def input_data(self, Emulator):
        for i in range(len(self.name_entry)):
            done = False
            try:
                Emulator.tape[i-len(self.name_entry)//2+Emulator.position]
            except KeyError:
                if i <= 0:
                    if self.name_entry[i].text() == '':
                        temp_dict = {i-len(self.name_entry)//2+Emulator.position : ' '} #?????????????
                        temp_dict.update(Emulator.tape)
                        Emulator.tape = temp_dict
                    else:
                        temp_dict = {i-len(self.name_entry)//2+Emulator.position : self.name_entry[i].text()} #?????????????
                        temp_dict.update(Emulator.tape)
                        Emulator.tape = temp_dict
                    done = True
                else:
                    if self.name_entry[i].text() == '':
                        Emulator.tape[i-len(self.name_entry)//2+Emulator.position] = ' '
                    else:
                        Emulator.tape[i-len(self.name_entry)//2+Emulator.position] = self.name_entry[i].text()
                    done = True
            if done == False:
                if self.name_entry[i].text() == '':
                    Emulator.tape[i-len(self.name_entry)//2+Emulator.position] = ' '
                else:
                    Emulator.tape[i-len(self.name_entry)//2+Emulator.position] = self.name_entry[i].text()               

    def get_data(self, Emulator):
        for i in range(len(self.name_entry)):
            try:
                self.name_entry[i].setText(Emulator.tape[i-13+Emulator.position])
            except KeyError:
                self.name_entry[i].setText('')
            if self.name_entry[i].text() == ' ':
               self.name_entry[i].setText('') 

    def change_button_icon(self, short_path, size1, size2, button):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/right_button'
        left_button_icon = QIcon()
        left_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self.left_button.setIcon(left_button_icon)
        self.left_button.setIconSize(QSize(25, 25))
    

    def left_buttonClicked(self):
        self.change_button_icon()
        QApplication.processEvents()
        self.input_data(self.emulator)
        self.emulator.position = self.emulator.position-1
        self.get_data(self.emulator)

    def right_buttonClicked(self):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/right_button'
        right_button_icon = QIcon()
        right_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self.right_button.setIcon(right_button_icon)
        self.right_button.setIconSize(QSize(25, 25))
        QApplication.processEvents()
        ########################
        time.sleep(0.1)
        self.input_data(self.emulator)
        self.emulator.position = self.emulator.position+1
        self.get_data(self.emulator)
        ########################
        path = current_directory + '/icons/right_button_activated'
        right_button_icon = QIcon()
        right_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self.right_button.setIcon(right_button_icon)
        self.right_button.setIconSize(QSize(25, 25))



    def run_buttonClicked(self):
        if self.run_activated == False:
            self.run_activated = True
            current_directory = str(pathlib.Path(__file__).parent.absolute())
            path = current_directory + '/icons/run_button_activated2'
            run_button_icon = QIcon()
            run_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
            self.run_button.setIcon(run_button_icon)
            self.run_button.setIconSize(QSize(36, 25))

            Machine = Get_Machine()
            self.input_data(self.emulator)
            print(self.emulator.tape)
            print(self.emulator.position)
            emulate = 1
            current_directory = str(pathlib.Path(__file__).parent.absolute())
            path = current_directory + '/sounds/test3.mp3'
            while (emulate == 1):
                emulate = self.emulator.emulate_one_step(Machine)
                self.get_data(self.emulator)
                QApplication.processEvents()
                #playsound(path)
                time.sleep(self.run_speed)
            QMessageBox().information(self, "Emulator", "Емулятор успішно закінчив свою роботу!", QMessageBox.Ok, QMessageBox.Ok)

            path = current_directory + '/icons/run_button4'
            run_button_icon = QIcon()
            run_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
            self.run_button.setIcon(run_button_icon)
            self.run_button.setIconSize(QSize(31, 25))
            self.run_activated = False
        else: 
            return
    
    def reset_buttonClicked(self):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/reset_button'
        reset_button_icon = QIcon()
        reset_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self.reset_button.setIcon(reset_button_icon)
        self.reset_button.setIconSize(QSize(25, 25))
        QApplication.processEvents()

        time.sleep(0.1)
        self.emulator.tape = copy.copy(self.saved_tape)
        self.emulator.position = copy.copy(self.saved_position)
        self.get_data(self.emulator)

        path = current_directory + '/icons/reset_button_activated'
        reset_button_icon = QIcon()
        reset_button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        self.reset_button.setIcon(reset_button_icon)
        self.reset_button.setIconSize(QSize(25, 25))

    def save_buttonClicked(self):
        return

# Run program
if __name__ == '__main__':
	palette = QPalette()
	palette.setColor(QPalette.Window, QColor(39, 41, 45))
	palette.setColor(QPalette.WindowText, Qt.white)
	palette.setColor(QPalette.Base, QColor(25, 25, 25))
	palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
	palette.setColor(QPalette.ToolTipBase, Qt.white)
	palette.setColor(QPalette.ToolTipText, Qt.white)
	palette.setColor(QPalette.Text, Qt.white)
	palette.setColor(QPalette.Button, QColor(53, 53, 53))
	palette.setColor(QPalette.ButtonText, Qt.white)
	palette.setColor(QPalette.BrightText, Qt.red)
	palette.setColor(QPalette.Link, QColor(42, 130, 218))
	palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
	palette.setColor(QPalette.HighlightedText, Qt.black)
	app = QApplication(sys.argv)
	app.setPalette(palette)
	window = Window()
	sys.exit(app.exec_())

