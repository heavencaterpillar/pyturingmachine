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
        self.run_button
        self.pause_button
        #self.stop_button
        #self.save_button
        self.reset_button
        
        self.run_speed = 0
        self.emulator = Turing_machine_emulator() 
        self.saved_tape = copy.copy(self.emulator.tape)
        self.saved_position = copy.copy(self.emulator.position)

        self.run_activated = False
        self.pause_activated = False
        self.stop_activated = False



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
        
        Right_button = QLabel(self)
        Right_button.resize(45, 80)
        Right_button.move(1395, 95)
        Right_button.setStyleSheet("background-color:rgb(54,54,54);") 
        Left_button = QLabel(self)
        Left_button.resize(45, 80)
        Left_button.move(0, 95)
        Left_button.setStyleSheet("background-color:rgb(54,54,54);") 
        ############

        ###Undertape panel####
        Undertape = QLabel(self)
        Undertape.resize(1440, 40)
        Undertape.move(0,210)
        Undertape.setStyleSheet("background-color:rgb(37,37,38);")
        ############  
         
        ###Table####
        Back_table = QLabel(self)
        Back_table.resize(1360, 700)
        Back_table.move(40,290)
        Back_table.setStyleSheet("background-color:rgb(37,37,38);")

        Front_table = QLabel(self)
        Front_table.resize(1300, 655)
        Front_table.move(100,335)
        Front_table.setStyleSheet("background-color:rgb(255,255,255);")
        
        lines1 = list()
        for i in range(0,23):
            lines1.append(QLabel(self))
            lines1[i].resize(1, 700)
            lines1[i].move(100+i*60,290)
            lines1[i].setStyleSheet("background-color:rgb(0,0,0);")

        lines2 = list()
        for i in range(0,15):
            lines2.append(QLabel(self))
            lines2[i].resize(1360, 1)
            lines2[i].move(40,335+i*45)
            lines2[i].setStyleSheet("background-color:rgb(0,0,0);")
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
            border: 1px black;
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
            border: 1px black;         
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
        Export_menu = menu_bar.addMenu('Export')
        Compile_menu = menu_bar.addMenu('Compile')
        
        file_menu.addAction(exit_act)

    def create_Toolbar_button(self, size1, size2, icon_size1, icon_size2, x, y, short_path, connection):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + short_path
        button_icon = QIcon()
        button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)

        button = QPushButton(self)
        button.clicked.connect(connection)
        button.resize(size1, size2)
        button.move(x, y)
        button.setIcon(button_icon)
        button.setIconSize(QSize(icon_size1, icon_size2))
        button.setStyleSheet("""
                                QPushButton::hover {
                                    border: none;
                                    background-color: rgb(50,50,50)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        return button 

    def displayToolbar(self):
        y_coord = 25
        x_coord = 0 
        #create_Toolbar_button(self, size1, size2, icon_size1, icon_size2, x, y, short_path)

        ####Run Button####
        self.run_button = self.create_Toolbar_button(74, 36, 31, 25, x_coord, y_coord, '/icons/run_button4', self.run_buttonClicked)
        ##################
        x_coord += 74

        ###Pause Button###
        self.pause_button = self.create_Toolbar_button(74, 36, 14, 25, x_coord, y_coord, '/icons/pause_button', self.pause_buttonClicked)
        ##################
        x_coord += 74

        ####Stop Button####
        self.stop_button = self.create_Toolbar_button(74, 36, 20, 25, x_coord, y_coord, '/icons/stop_button5', self.stop_buttonClicked)
        ###################
        x_coord += 74

        ####Save Button####
        self.save_button = self.create_Toolbar_button(74, 36, 25, 25, x_coord, y_coord, '/icons/save_button', self.save_buttonClicked)
        ###################
        x_coord += 74
        
        ####Reset Button####
        self.reset_button = self.create_Toolbar_button(74, 36, 25, 25, x_coord, y_coord, '/icons/reset_button', self.reset_buttonClicked)
        ####################
        x_coord += 74

        ####Clear Button####
        self.clear_button = self.create_Toolbar_button(74, 36, 25, 25, x_coord, y_coord, '/icons/clear_button', self.clear_buttonClicked)
        ####################
        x_coord += 74

        ####Step Button####
        self.step_button = self.create_Toolbar_button(74, 36, 36, 25, x_coord, y_coord, '/icons/step_button', self.step_buttonClicked)
        ####################
        x_coord += 74

        ####Fisrt state Button####
        self.first_state_button = self.create_Toolbar_button(74, 36, 25, 25, x_coord, y_coord, '/icons/first_state_button', self.first_state_buttonClicked)
        ####################
        x_coord += 74


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
        path = current_directory + '/icons/left_button2'
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
        path = current_directory + '/icons/right_button2'
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
            self.name_entry[i].setStyleSheet("background-color:rgb(255,255,240); color:rgb(78,78,78);")
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
        path = current_directory + short_path
        button_icon = QIcon()
        button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        button.setIcon(button_icon)
        button.setIconSize(QSize(size1, size2))
    

    def left_buttonClicked(self):
        self.change_button_icon('/icons/left_button2_activated', 20, 80, self.left_button)
        QApplication.processEvents()
        time.sleep(0.05)
        #################
        self.input_data(self.emulator)
        self.emulator.position = self.emulator.position-1
        self.get_data(self.emulator)
        #################
        self.change_button_icon('/icons/left_button2', 20, 80, self.left_button)

    def right_buttonClicked(self):
        self.change_button_icon('/icons/right_button2_activated', 20, 80, self.right_button)
        QApplication.processEvents()
        time.sleep(0.05)
        ########################
        self.input_data(self.emulator)
        self.emulator.position = self.emulator.position+1
        self.get_data(self.emulator)
        ########################
        self.change_button_icon('/icons/right_button2', 20, 80, self.right_button)

    def pause_buttonClicked(self):
        if self.run_activated == False:
            self.change_button_icon('/icons/pause_button_activated', 10, 25, self.pause_button)
            QApplication.processEvents()
            time.sleep(0.05)
            self.change_button_icon('/icons/pause_button', 14, 25, self.pause_button)
            return
        self.change_button_icon('/icons/pause_button_activated', 14, 25, self.pause_button)
        QApplication.processEvents()
        #################
        self.pause_activated = True
        #################
        return

    def stop_buttonClicked(self):
        if self.run_activated == False:
            self.change_button_icon('/icons/stop_button5_activated', 14, 25, self.stop_button)
            QApplication.processEvents()
            time.sleep(0.05)
            self.change_button_icon('/icons/stop_button5', 25, 25, self.stop_button)
            return
        self.change_button_icon('/icons/stop_button5_activated', 14, 25, self.stop_button)
        QApplication.processEvents()
        #################
        self.stop_activated = True
        #################
        return

    def clear_buttonClicked(self):
        if self.run_activated == True:
            self.change_button_icon('/icons/clear_button_activated', 14, 25, self.clear_button)
            QApplication.processEvents()
            time.sleep(0.05)
            self.change_button_icon('/icons/clear_button', 25, 25, self.stop_button)
            QMessageBox().information(self, "Clear", "Ви не можете стерти ленту під час роботи емулятора!", QMessageBox.Ok, QMessageBox.Ok)
            return
        self.change_button_icon('/icons/clear_button_activated', 14, 25, self.clear_button)
        QApplication.processEvents()
        time.sleep(0.05)
        self.change_button_icon('/icons/clear_button', 25, 25, self.clear_button)
        clear_tape = tape = [" "]*27
        self.emulator_tape = dict() 
        for i in range(-13, len(clear_tape)//2 + 1):
            self.emulator.tape[i] = clear_tape[i+13] 
        self.emulator.position = 0
        self.get_data(self.emulator)
        return

    def step_buttonClicked(self):
        
        self.change_button_icon('/icons/step_button_activated', 36, 25, self.step_button)
        QApplication.processEvents()
        time.sleep(0.05)
        Machine = Get_Machine()
        self.input_data(self.emulator)
        print(self.emulator.tape)
        print(self.emulator.position)
        emulate = 1
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        #path = current_directory + '/sounds/test3.mp3'
        emulate = self.emulator.emulate_one_step(Machine)
        self.get_data(self.emulator)
        QApplication.processEvents()
        #playsound(path)
        if emulate == 0:
            QMessageBox().information(self, "Emulator", "Емулятор успішно закінчив свою роботу!", QMessageBox.Ok, QMessageBox.Ok)
        self.change_button_icon('/icons/step_button', 36, 25, self.step_button)

        return

    def stop_buttonClicked(self):
        if self.run_activated == False:
            self.change_button_icon('/icons/stop_button5_activated', 14, 25, self.stop_button)
            QApplication.processEvents()
            time.sleep(0.05)
            self.change_button_icon('/icons/stop_button5', 25, 25, self.stop_button)
            return
        self.change_button_icon('/icons/stop_button5_activated', 14, 25, self.stop_button)
        QApplication.processEvents()
        #################
        self.stop_activated = True
        #################
        return

    def run_buttonClicked(self):
        if self.run_activated == False:
            if self.pause_activated == True:
                self.pause_activated = False
                self.change_button_icon('/icons/pause_button', 14, 25, self.pause_button)
            self.run_activated = True
            self.change_button_icon('/icons/run_button_activated2', 36, 35, self.run_button)
            QApplication.processEvents()
            time.sleep(0.05)

            Machine = Get_Machine()
            self.input_data(self.emulator)
            print(self.emulator.tape)
            print(self.emulator.position)
            emulate = 1
            current_directory = str(pathlib.Path(__file__).parent.absolute())
            #path = current_directory + '/sounds/test3.mp3'
            while (emulate == 1):
                if self.pause_activated == True:
                    self.run_activated = False
                    self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
                    return
                if self.stop_activated == True:
                    self.stop_activated = False
                    self.emulator.state = 1
                    self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
                    time.sleep(0.05)
                    self.change_button_icon('/icons/stop_button5', 25, 25, self.stop_button)
                    self.run_activated = False
                    return
                emulate = self.emulator.emulate_one_step(Machine)
                self.get_data(self.emulator)
                QApplication.processEvents()
                #playsound(path)
                time.sleep(self.run_speed)
            self.emulator.state = 1
            QMessageBox().information(self, "Emulator", "Емулятор успішно закінчив свою роботу!", QMessageBox.Ok, QMessageBox.Ok)

            self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
            
            self.run_activated = False
        else: 
            return
    
    def reset_buttonClicked(self):
        self.change_button_icon('/icons/reset_button_activated', 20, 25, self.reset_button)
        QApplication.processEvents()
        time.sleep(0.05)
        self.emulator.tape = copy.copy(self.saved_tape)
        self.emulator.position = copy.copy(self.saved_position)
        self.get_data(self.emulator)

        self.change_button_icon('/icons/reset_button', 25, 25, self.reset_button)
        
    def first_state_buttonClicked(self):
        self.change_button_icon('/icons/first_state_button_activated', 20, 25, self.first_state_button)
        QApplication.processEvents()
        time.sleep(0.05)
        self.emulator.state = 1
        self.change_button_icon('/icons/first_state_button', 25, 25, self.first_state_button)

    def save_buttonClicked(self):
        self.change_button_icon('/icons/save_button_activated', 20, 25, self.save_button)
        QApplication.processEvents()
        
        self.input_data(self.emulator)
        self.saved_tape = copy.copy(self.emulator.tape)
        self.saved_position = copy.copy(self.emulator.position)
        time.sleep(0.05)
        self.change_button_icon('/icons/save_button', 25, 25, self.save_button)
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

