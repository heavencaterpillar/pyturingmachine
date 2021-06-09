from typing import Text
from playsound import playsound
import os, sys, pathlib, time, copy, pickle

from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QPixmap, QKeySequence, QBrush
from PyQt5 import QtCore
from PyQt5.Qt import QTransform

sys.path.append("")

from machine.emulator import Turing_machine_emulator
from machine.getmachine import Get_Machine
from machine.decoder import Decoder
from Table.Table import Table_panel


class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() # Initializer which calls constructor for QWidgself.initializeUI() # Call function used to set up window
        self.initializeUI()
        self.run_button
        self.pause_button
        #self.stop_button
        #self.save_button
        self.reset_button
        self.pointer

        self.run_speed = 0
        self.no_animations = False
        self.emulator = Turing_machine_emulator() 
        self.saved_tape = copy.copy(self.emulator.tape)
        self.saved_position = copy.copy(self.emulator.position)
        
        #self.alphabet_line 
        self.Table_panel

        self.run_activated = False
        self.pause_activated = False
        self.stop_activated = False

        self.file_path = None
        self.file_label = None

        self.decoder = Decoder()

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
        Toolbar_y = 30
        Toolbar = QLabel(self)
        Toolbar.resize(1440, 84)
        Toolbar.move(0,0)
        Toolbar.setStyleSheet("background-color:rgb(54,54,54);")

        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/State_text'
        State_text_pic = QPixmap(path)
        State_text = QLabel(self)
        State_text.resize(140, 27)
        State_text.move(1150+40, Toolbar_y)
        State_text.setPixmap(State_text_pic)
        ############

        ###Tape panel####
        Tape = QLabel(self)
        Tape.resize(1440, 152)
        Tape.move(0,65)
        Tape.setStyleSheet("background-color:rgb(49,54,59);") # 39, 41, 45);")
        
        Right_button = QLabel(self)
        Right_button.resize(45, 80)
        Right_button.move(1395, 95)
        Right_button.setStyleSheet("background-color:rgb(54,54,54);") 
        Left_button = QLabel(self)
        Left_button.resize(45, 80)
        Left_button.move(0, 95)
        Left_button.setStyleSheet("background-color:rgb(54,54,54);") 
        #################

        ###Undertape panel####
        Undertape = QLabel(self)
        Undertape.resize(1440, 30)
        Undertape.move(0,210)
        Undertape.setStyleSheet("background-color:rgb(37,37,38);")
        ######################  
        
        #####Table panel#######
        Table = Table_panel(self)
        self.Table_panel = Table
        #######################
        



    def createMenu(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        save = QAction('Save', self)
        save.setShortcut('Ctrl+S')
        save.triggered.connect(self.file_save)
        save_as = QAction('Save as...', self)
        save_as.setShortcut('Ctrl+Shift+S')
        save_as.triggered.connect(self.file_save_as)
        

        open_file = QAction('Open', self)
        open_file.setShortcut('Ctrl+O')
        open_file.triggered.connect(self.file_open)

        decode_import_dikarev = QAction('Import Dikarev', self)
        decode_import_dikarev.triggered.connect(self.decoder_import_dikarev)
        decode_export_dikarev = QAction('Export Dikarev', self)
        decode_export_dikarev.triggered.connect(self.decoder_export_dikarev)

        wait_for = QAction('Wait for next version 🙃', self)

        speed_025 = QAction('0.25x', self)
        speed_05 = QAction('0.5x', self)
        speed_1 = QAction('1x', self)
        speed_2 = QAction('2x', self)
        speed_4 = QAction('4x', self)
        speed_max = QAction('Max', self)
        speed_beyond_max = QAction('Beyond max', self)

        speed_025.triggered.connect(self.speed_025x)
        speed_05.triggered.connect(self.speed_05x)
        speed_1.triggered.connect(self.speed_1x)
        speed_2.triggered.connect(self.speed_2x)
        speed_4.triggered.connect(self.speed_4x)
        speed_max.triggered.connect(self.speed_max)
        speed_beyond_max.triggered.connect(self.speed_beyond_max)

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
        speed_menu = menu_bar.addMenu('Speed')
        Decoder_menu = menu_bar.addMenu('Decoder')
        Compile_menu = menu_bar.addMenu('Compile')


        speed_menu.addAction(speed_025)
        speed_menu.addAction(speed_05)
        speed_menu.addAction(speed_1)
        speed_menu.addAction(speed_2)
        speed_menu.addAction(speed_4)
        speed_menu.addAction(speed_max)
        speed_menu.addAction(speed_beyond_max)
        
        file_menu.addAction(save)
        file_menu.addAction(save_as)
        file_menu.addAction(open_file)
        file_menu.addAction(exit_act)

        Decoder_menu.addAction(decode_import_dikarev)
        Decoder_menu.addAction(decode_export_dikarev)
        Compile_menu.addAction(wait_for)
        
####################################################################################################################
#                                                      Menu functions                                              #
####################################################################################################################

    ################Speed functions##############
    def speed_025x(self):
        self.run_speed = 1 
        self.no_animations = False

    def speed_05x(self):
        self.run_speed = 0.5 
        self.no_animations = False
    
    def speed_1x(self):
        self.run_speed = 0.25 
        self.no_animations = False

    def speed_2x(self):
        self.run_speed = 0.125
        self.no_animations = False 
    
    def speed_4x(self):
        self.run_speed = 0.075
        self.no_animations = False 

    def speed_max(self):
        self.run_speed = 0
        self.no_animations = False 

    def speed_beyond_max(self):
        self.run_speed = 0
        self.no_animations = True
    ##############################################

    ##################File functions##############
    def create_file_label(self, path):
        self.file_label.hide()
        file_name = 'unnamed'
        file_name = copy.copy(path)
        file_name = file_name.split('/')
        file_name[-1] = file_name[-1].split('.')
        file_name = file_name[-1][0]

        print("Hello")
        self.file_label = QLabel(self)
        self.file_label.resize(60+len(file_name)*10, 30)
        self.file_label.move(0, 210) 
        self.file_label.setStyleSheet("background-color:rgb(39,41,45); color:#FF76FF") #background-color:rgb(39,41,45);       
        self.file_label.show()
        print("Hello")

        Font = QFont("Roboto",16)
        self.file_label.setFont(Font)
        self.file_label.setText(file_name)
        self.file_label.setAlignment(Qt.AlignCenter)
        return


    def file_save(self):
        if self.run_activated == True:
            self.information_box("Не можливо зберегти файл під час роботи емулятора!")
            return

        if self.file_path == None:
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("*.pkl")
            file_name = file_dialog.getSaveFileName(self, "Open a file", "", "(*.pkl)")
            self.file_path = file_name[0]

            
            print(self.file_path)
            with open(self.file_path, 'wb') as output:
                info = Save_to_file(self.saved_tape, self.saved_position, self.Table_panel.machine)
                pickle.dump(info, output)
                del info

            self.create_file_label(self.file_path)
        
        else:
            self.file_label.setStyleSheet("background-color:rgb(37,37,38); color:#D663D6")
            print(self.file_path)
            with open(self.file_path, 'wb') as output:
                info = Save_to_file(self.saved_tape, self.saved_position, self.Table_panel.machine)
                pickle.dump(info, output)
                del info
            QApplication.processEvents()
            time.sleep(0.15)
            self.file_label.setStyleSheet("background-color:rgb(39,41,45); color:#FF76FF")

    def file_save_as(self):
        if self.run_activated == True:
            self.information_box("Не можливо зберегти файл під час роботи емулятора!")
            return

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("*.pkl")
        file_name = file_dialog.getSaveFileName(self, "Open a file", "", "(*.pkl)")
        self.file_path = file_name[0]
        
        print(self.file_path)
        with open(self.file_path, 'wb') as output:
            info = Save_to_file(self.saved_tape, self.saved_position, self.Table_panel.machine)
            pickle.dump(info, output)
            del info
        self.create_file_label(self.file_path)
        return
        
        
            

    def file_open(self):
        if self.run_activated == True:
            self.information_box("Не можливо відкрити файл під час роботи емулятора!")
            return  

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("*.pkl")
        
        file_name = file_dialog.getOpenFileName(self, "Open a file", "", "(*.pkl)")
        self.file_path = file_name[0]

        print(self.file_path)
        with open(self.file_path, 'rb') as input:
                info = pickle.load(input) #emulator, tape, position, machine
                self.saved_position = info.position
                self.saved_tape = info.tape
                self.Table_panel.machine = info.machine
                self.emulator.tape = copy.copy(self.saved_tape)
                self.emulator.position = copy.copy(self.saved_position)
                self.emulator.state = 1
                #del info
        self.Table_panel.alphabet_line.setText(("").join(self.Table_panel.machine.alphabet))
        self.update_data()



        self.create_file_label(self.file_path)       
    ####################################################################

    #########################Decoder functions##########################
    def decoder_import_dikarev(self):
        if self.run_activated == True:
            self.information_box("Не можливо декодувати файл під час роботи емулятора!")
            return

        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("*.txt")
        
        file_name = file_dialog.getOpenFileName(self, "Open a file", "", "(*.txt)")
        self.file_path = file_name[0]

        self.Table_panel.machine = self.decoder.Dikarev_decoder(self.file_path)
        self.Table_panel.machine.alphabet.remove(' ')
        self.Table_panel.machine.alphabet.append(' ')
        print(self.Table_panel.machine.alphabet)
        self.Table_panel.alphabet_line.setText(("").join(self.Table_panel.machine.alphabet[0:len(self.Table_panel.machine.alphabet)-1]))
        self.create_file_label(self.file_path)
        self.file_path = None
        self.update_data()


    def decoder_export_dikarev(self):
        if self.run_activated == True:
            self.information_box("Не можливо закодувати файл під час роботи емулятора!")
            return
        
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("*.txt")
        file_name = file_dialog.getSaveFileName(self, "Open a file", "", "(*.txt)")
        self.file_path = file_name[0]
        self.decoder.Dikarev_encoder(self.Table_panel.machine, self.file_path) 
    ###########################################################################



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
        self.run_button = self.create_Toolbar_button(74, 41, 31, 25, x_coord, y_coord, '/icons/run_button4', self.run_buttonClicked)
        ##################
        x_coord += 74

        ###Pause Button###
        self.pause_button = self.create_Toolbar_button(74, 41, 14, 25, x_coord, y_coord, '/icons/pause_button', self.pause_buttonClicked)
        ##################
        x_coord += 74

        ####Stop Button####
        self.stop_button = self.create_Toolbar_button(74, 41, 20, 25, x_coord, y_coord, '/icons/stop_button5', self.stop_buttonClicked)
        ###################
        x_coord += 74
        x_coord += 37

        ####Save Button####
        self.save_button = self.create_Toolbar_button(74, 41, 25, 25, x_coord, y_coord, '/icons/save_button', self.save_buttonClicked)
        ###################
        x_coord += 74
        
        ####Reset Button####
        self.reset_button = self.create_Toolbar_button(74, 41, 25, 25, x_coord, y_coord, '/icons/reset_button', self.reset_buttonClicked)
        ####################
        x_coord += 74

        ####Clear Button####
        self.clear_button = self.create_Toolbar_button(74, 41, 25, 25, x_coord, y_coord, '/icons/clear_button', self.clear_buttonClicked)
        ####################
        x_coord += 74
        x_coord += 37

        ####Step Button####1
        self.step_button = self.create_Toolbar_button(74, 41, 36, 25, x_coord, y_coord, '/icons/step_button', self.step_buttonClicked)
        ####################
        x_coord += 74

        ####Fisrt state Button####
        self.first_state_button = self.create_Toolbar_button(74, 41, 25, 25, x_coord, y_coord, '/icons/first_state_button', self.first_state_buttonClicked)
        ####################
        x_coord += 74

        ###########State line###########
        self.state_line = QLineEdit(self)
        self.state_line.setAlignment(Qt.AlignCenter) # The default alignmeis AlignLeft
        self.state_line.move(1150+137+5+40, y_coord+3)
        self.state_line.resize(74, 30) # Change size of entry field
        self.state_line.setMaxLength(4)
        self.state_line.setStyleSheet("background-color:rgb(49,54,59); color:rgb(255,0,255);") #37,37,38 #49,54,59
        self.state_line.setFont(QFont("Bruno Ace",30))
        self.state_line.setText('1')
        self.state_line.isUndoAvailable = True
        self.state_line.editingFinished.connect(self.state_line_edited)    
        ################################


    def call_warning_box(self):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/warning'
        messagebox = QMessageBox(QMessageBox.Warning, "Warning", "Стан може бути тільки цілим числом!", QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap(path))
        messagebox.setFont(QFont("Bruno Ace",14))
        exe = messagebox.exec_()

    def information_box(self, message_text):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/information'
        messagebox = QMessageBox(QMessageBox.Warning, "Information", message_text, QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap(path))
        messagebox.setFont(QFont("Bruno Ace",14))
        exe = messagebox.exec_()

    def finish_box(self):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/finish_message'
        messagebox = QMessageBox(QMessageBox.Warning, "Finish", "Емулятор успішно закінчив свою роботу!", QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap(path))
        messagebox.setFont(QFont("Bruno Ace",14))
        exe = messagebox.exec_()
    
    def error_finish_box(self, state, symbol):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + '/icons/error_finish_message'
        messagebox = QMessageBox(QMessageBox.Warning, "Error", "У стані Q"+str(state)+" немає команди для символу "+"«"+str(symbol)+"»...", QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap(path))
        messagebox.setFont(QFont("Bruno Ace",12))
        exe = messagebox.exec_()

     

    def state_line_edited(self):
        #if self.run_activated == True:
        #    self.state_line.setText(str(self.emulator.state))
        #    QApplication.processEvents()
        #    self.information_box("Ви не змінити стан під час роботи емулятора!")
        #    return
        try:
            int(self.state_line.text())
        except ValueError:
            self.state_line.setStyleSheet("background-color:rgb(49,54,59); color:rgb(240,20,20);")
            QApplication.processEvents()
            time.sleep(0.1)
            self.state_line.setStyleSheet("background-color:rgb(49,54,59); color:rgb(255,0,255);")
            self.state_line.setText(str(self.emulator.state))
            self.call_warning_box()
        self.state_line.setStyleSheet("background-color:rgb(49,54,59); color:rgb(210,0,210);")
        QApplication.processEvents()
        time.sleep(0.1)
        self.state_line.setStyleSheet("background-color:rgb(49,54,59); color:rgb(255,0,255);")
        #self.alphabet_line.setStyleSheet("background-color:rgb(0,255,0); color:rgb(78,78,78);")
        #QApplication.processEvents()
        #time.sleep(0.1)
        #self.alphabet_line.setStyleSheet("background-color:rgb(255,255,240); color:rgb(78,78,78);")


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
        self.pointer = pointer
        ######### 
         
        ####Left Button####
        left_button = self.create_Toolbar_button(45, 80, 20, 80, 0, 95, '/icons/left_button2', self.left_buttonClicked)
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
        right_button = self.create_Toolbar_button(45, 80, 20, 80, 1395, 95, '/icons/right_button2', self.right_buttonClicked)
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
            self.name_entry[i].setAlignment(Qt.AlignCenter) # The default alignmeis AlignLeft
            self.name_entry[i].move(45+i*50, 95)
            self.name_entry[i].resize(46, 80) # Change size of entry field
            self.name_entry[i].setMaxLength(1)
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

    ####################################################################################################################
    #                                                   Buttons clicked functions                                      #
    ####################################################################################################################

    def change_button_icon(self, short_path, size1, size2, button):
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        path = current_directory + short_path
        button_icon = QIcon()
        button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        button.setIcon(button_icon)
        button.setIconSize(QSize(size1, size2))
    

    def left_buttonClicked(self):
        if self.run_activated == True:
            self.change_button_icon('/icons/left_button2_activated', 20, 80, self.left_button)
            QApplication.processEvents()
            time.sleep(0.01)
            self.change_button_icon('/icons/left_button2', 20, 80, self.left_button)
            QApplication.processEvents()
            self.information_box("Ви не можете змістити ленту вліво під час роботи емулятора!")
            return
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
        if self.run_activated == True:
            self.change_button_icon('/icons/right_button2_activated', 20, 80, self.right_button)
            QApplication.processEvents()
            time.sleep(0.01)
            self.change_button_icon('/icons/right_button2', 20, 80, self.right_button)
            QApplication.processEvents()
            self.information_box("Ви не можете змістити ленту вправо під час роботи емулятора!")
            return
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
            time.sleep(0.01)
            self.change_button_icon('/icons/clear_button', 25, 25, self.clear_button)
            QApplication.processEvents()
            self.information_box("Ви не можете стерти ленту під час роботи емулятора!")
            return
        self.change_button_icon('/icons/clear_button_activated', 14, 25, self.clear_button)
        QApplication.processEvents()
        time.sleep(0.05)
        self.change_button_icon('/icons/clear_button', 25, 25, self.clear_button)
        clear_tape = tape = ['']*27
        self.emulator.tape = dict() 
        for i in range(-13, len(clear_tape)//2 + 1):
            self.emulator.tape[i] = clear_tape[i+13] 
        self.emulator.position = 0
        self.get_data(self.emulator)
        return

    def step_buttonClicked(self):
        if self.run_activated == True:
            self.change_button_icon('/icons/step_button_activated', 36, 25, self.step_button)
            QApplication.processEvents()
            time.sleep(0.01)
            self.change_button_icon('/icons/step_button', 36, 25, self.step_button)
            QApplication.processEvents()
            self.information_box("Емулятор вже запущений!")
            return

        self.change_button_icon('/icons/step_button_activated', 36, 25, self.step_button)
        QApplication.processEvents()
        time.sleep(0.05)
        Machine = self.Table_panel.machine
        self.input_data(self.emulator)
        emulate = 1
        current_directory = str(pathlib.Path(__file__).parent.absolute())
        #path = current_directory + '/sounds/test3.mp3'
        emulate = self.emulator.emulate_one_step(Machine)
        self.get_data(self.emulator)
        QApplication.processEvents()
        #playsound(path)
        self.state_line.setText(str(self.emulator.state))
        if emulate == 0:
            self.finish_box()
            self.emulator.state = 1
            self.state_line.setText('1')
        elif emulate != 1:
            if emulate[1] == " ":
                self.error_finish_box(emulate[0], "λ")
            else:
                self.error_finish_box(emulate[0], emulate[1])

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

    def no_animations_run(self, Machine):
        processing = ['', '', '', '', '', '', '', '' ,'P', 'r', 'o', 'c', 'e', 's', 's', 'i', 'n', 'g', '.', '.', '.', '', '', '', '', '', '', '']
        self.state_line.setText('?')
        self.pointer.hide()
        for i in range(len(self.name_entry)):
            self.name_entry[i].setText(processing[i])
            self.name_entry[i].setStyleSheet("background-color:rgb(203,252,255); color:rgb(255,0,255);")
            self.name_entry[i].setFont(QFont("Bruno Ace",50))
        QApplication.processEvents()
        emulate = 1
        while (emulate == 1):
            if self.pause_activated == True:
                self.run_activated = False
                for i in range(len(self.name_entry)):
                    self.name_entry[i].setText('')
                    self.name_entry[i].setStyleSheet("background-color:rgb(255,255,240); color:rgb(78,78,78);")
                    self.name_entry[i].setFont(QFont("Roboto",50))
                self.state_line.setText(str(self.emulator.state))
                self.get_data(self.emulator)
                self.pointer.show()
                QApplication.processEvents()
                
                self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
                return emulate

            if self.stop_activated == True:
                self.stop_activated = False
                self.get_data(self.emulator)
                for i in range(len(self.name_entry)):
                    self.name_entry[i].setText('')
                    self.name_entry[i].setStyleSheet("background-color:rgb(255,255,240); color:rgb(78,78,78);")
                    self.name_entry[i].setFont(QFont("Roboto",50))
                self.state_line.setText(str(self.emulator.state))
                self.pointer.show()
                QApplication.processEvents()
                self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
                time.sleep(0.05)
                self.change_button_icon('/icons/stop_button5', 25, 25, self.stop_button)
                self.run_activated = False
                return emulate

            if self.no_animations == True:
                emulate = self.emulator.emulate_one_step(Machine)
            else:
                self.pointer.show()
                self.get_data(self.emulator)
                for i in range(len(self.name_entry)):
                    self.name_entry[i].setText('')
                    self.name_entry[i].setStyleSheet("background-color:rgb(255,255,240); color:rgb(78,78,78);")
                    self.name_entry[i].setFont(QFont("Roboto",50))
                self.state_line.setText(str(self.emulator.state))
                QApplication.processEvents()
                return emulate

        self.pointer.show()
        self.get_data(self.emulator)
        for i in range(len(self.name_entry)):
            self.name_entry[i].setText('')
            self.name_entry[i].setStyleSheet("background-color:rgb(255,255,240); color:rgb(78,78,78);")
            self.name_entry[i].setFont(QFont("Roboto",50))
        self.state_line.setText(str(self.emulator.state))
        QApplication.processEvents()
        return emulate


    def run_buttonClicked(self):
        if self.run_activated == False:
            self.state_line.setReadOnly(True)
            if self.pause_activated == True:
                self.pause_activated = False
                self.change_button_icon('/icons/pause_button', 14, 25, self.pause_button)
            self.run_activated = True
            self.change_button_icon('/icons/run_button_activated2', 36, 35, self.run_button)
            QApplication.processEvents()
            time.sleep(0.05)

            Machine = self.Table_panel.machine
            self.input_data(self.emulator)
            emulate = 1
            current_directory = str(pathlib.Path(__file__).parent.absolute())
            #path = current_directory + '/sounds/test3.mp3'
            while (emulate == 1):
                if self.pause_activated == True:
                    self.run_activated = False
                    self.state_line.setReadOnly(False)
                    self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
                    self.get_data(self.emulator)
                    self.state_line.setText(str(self.emulator.state))
                    QApplication.processEvents()
                    return

                if self.stop_activated == True:
                    self.stop_activated = False
                    self.emulator.state = 1
                    self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
                    time.sleep(0.05)
                    self.change_button_icon('/icons/stop_button5', 25, 25, self.stop_button)
                    self.run_activated = False
                    self.state_line.setReadOnly(False)
                    self.get_data(self.emulator)
                    self.state_line.setText(str(self.emulator.state))
                    QApplication.processEvents()
                    return
                
                if self.no_animations == False:
                    #self.Table_panel.table.item(Machine.alphabet.index(self.emulator.tape[self.emulator.position]), int(self.emulator.state)).setBackground(QBrush(QColor('red'))) #166,255,165
                    #self.Table_panel.table.item(Machine.alphabet.index(self.emulator.tape[self.emulator.position]), int(self.emulator.state)).setForeground(QBrush(QColor('red')))
                    emulate = self.emulator.emulate_one_step(Machine)
                    self.get_data(self.emulator)
                    self.state_line.setText(str(self.emulator.state))
                    QApplication.processEvents()
                    
                    time.sleep(self.run_speed)
                else:
                    emulate = self.no_animations_run(Machine)
            
            self.get_data(self.emulator)
            self.emulator.state = 1

            if emulate == 0:
                self.finish_box()
            else:
                if emulate[1] == " ":
                    self.error_finish_box(emulate[0], "λ")
                else:
                    self.error_finish_box(emulate[0], emulate[1])

            self.change_button_icon('/icons/run_button4', 31, 25, self.run_button)
            self.state_line.setText('1')
            self.run_activated = False
            self.state_line.setReadOnly(False)
        else: 
            return
    
    def reset_buttonClicked(self):
        if self.run_activated == True:
            self.change_button_icon('/icons/clear_button_activated', 14, 25, self.reset_button)
            QApplication.processEvents()
            time.sleep(0.01)
            self.change_button_icon('/icons/clear_button', 25, 25, self.reset_button)
            QApplication.processEvents()
            self.information_box("Ви не можете відновити ленту під час роботи емулятора!")
            return
        self.change_button_icon('/icons/reset_button_activated', 20, 25, self.reset_button)
        QApplication.processEvents()
        time.sleep(0.05)
        self.emulator.tape = copy.copy(self.saved_tape)
        self.emulator.position = copy.copy(self.saved_position)
        self.get_data(self.emulator)

        self.change_button_icon('/icons/reset_button', 25, 25, self.reset_button)
        
    def first_state_buttonClicked(self):
        if self.run_activated == True:
            self.change_button_icon('/icons/first_state_button_activated', 20, 25, self.first_state_button)
            QApplication.processEvents()
            time.sleep(0.01)
            self.change_button_icon(('/icons/first_state_button', 25, 25, self.first_state_button))
            QApplication.processEvents()
            self.information_box("Ви не змінити стан під час роботи емулятора!")
            return
        self.change_button_icon('/icons/first_state_button_activated', 20, 25, self.first_state_button)
        self.state_line.setText('1')
        QApplication.processEvents()
        time.sleep(0.05)
        self.emulator.state = 1
        self.change_button_icon('/icons/first_state_button', 25, 25, self.first_state_button)

    def save_buttonClicked(self):
        if self.run_activated == True:
            self.change_button_icon('/icons/clear_button_activated', 14, 25, self.save_button)
            QApplication.processEvents()
            time.sleep(0.05)
            self.change_button_icon('/icons/clear_button', 25, 25, self.save_button)
            QApplication.processEvents()
            self.information_box("Ви не можете зберенти ленту під час роботи емулятора!")
            return
        self.change_button_icon('/icons/save_button_activated', 20, 25, self.save_button)
        QApplication.processEvents()
        
        self.input_data(self.emulator)
        self.saved_tape = copy.copy(self.emulator.tape)
        self.saved_position = copy.copy(self.emulator.position)
        time.sleep(0.05)
        self.change_button_icon('/icons/save_button', 25, 25, self.save_button)
        return

    def state_text_buttonClicked(self):
        return

    def update_data(self):
        self.get_data(self.emulator)
        self.Table_panel.updateTable()


####################################################################################################################
#                                                   File class                                                     #
####################################################################################################################
class Save_to_file():
    def __init__(self, tape1, position1, machine1):
        self.tape = tape1
        self.position = position1
        self.machine = machine1
    
####################################################################################################################
#                                                   Run program                                                    #
####################################################################################################################


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

