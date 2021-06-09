from PyQt5.QtWidgets import QWidget

from playsound import playsound
import os, sys, pathlib, time, copy

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QPixmap, QKeySequence
from PyQt5 import QtCore
from PyQt5.Qt import QTransform

current_directory = str(pathlib.Path(__file__).parent.parent.absolute())
new_path = current_directory + '/machine'
sys.path.append(new_path)
from emulator import Turing_machine

def split(word):
    return [char for char in word]

class Table_panel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.machine = Turing_machine()

        self.text_change_again = False

        self.resize(1440, 770)
        self.move(0,250)
        self.setStyleSheet("background-color:rgb(39,41,45);") 

        self.machine.alphabet = ['0', '1', ' ']
        self.states = []
        for i in range(1, 30):
            self.states.append(str(i)) 

        #self.plus_button = QPushButton(self)
        #self.minus_button = QPushButton(self)

        self.initAlphabet()
        self.initButtons()
        self.initTable(len(self.machine.alphabet))
        self.table
    
    ####################################################################################################################
    #                                                   Alphabet                                                       #
    ####################################################################################################################

    def initAlphabet(self):
        x_coord = 40
        y_coord = 9
        self.alphabet_line = QLineEdit(self)
        self.alphabet_line.setAlignment(Qt.AlignCenter) # The default alignmeis AlignLeft
        self.alphabet_line.move(x_coord+170, y_coord)
        self.alphabet_line.resize(253, 27) # Change size of entry field
        self.alphabet_line.setStyleSheet("background-color:#252526; color:rgb(240,0,240);") #
        self.alphabet_line.setFont(QFont("Roboto",20))
        self.alphabet_line.setText(("").join(self.machine.alphabet[0:len(self.machine.alphabet)-1]))
        self.alphabet_line.editingFinished.connect(self.alphabet_line_change)

        current_directory = str(pathlib.Path(__file__).parent.parent.absolute())
        path = current_directory + '/icons/alphabet'
        State_text_pic = QPixmap(path)
        State_text = QLabel(self)
        State_text.resize(163, 27)
        State_text.move(x_coord, y_coord)
        State_text.setPixmap(State_text_pic)
    

    

    def alphabet_line_change(self):
        self.alphabet_line.setStyleSheet("background-color:#262627; color:rgb(210,0,210);")  #129,255,30
        QApplication.processEvents()
        new_alphabet = split(self.alphabet_line.text())

        new_alphabet = list(dict.fromkeys(new_alphabet))

        old_symbols = [' ']
        for i in new_alphabet:
            if i in self.machine.alphabet:
                old_symbols.append(i)
        
        for i in self.machine.alphabet:
            if i in old_symbols:
                pass
            else:
                #print(i)
                self.machine.delete_symbol(i)
        
        try:
            new_alphabet.remove(' ')
            #Предупреждение
        except ValueError:
            pass

        try:
            new_alphabet.remove('λ')
        except ValueError:
            pass

        new_alphabet.append(' ')

        self.alphabet_line.setText(("").join(new_alphabet[0:len(new_alphabet)-1]))
        self.machine.alphabet = new_alphabet
        #print(self.machine.alphabet)

        self.updateTable_rows()
        self.updateTable_items()

        time.sleep(0.1)
        self.alphabet_line.setStyleSheet("background-color:#252526; color:rgb(240,0,240);")
        return

    ####################################################################################################################
    #                                                   Buttons                                                        #
    ####################################################################################################################

    def create_button(self, size1, size2, icon_size1, icon_size2, x, y, short_path, connection):

        current_directory = str(pathlib.Path(__file__).parent.parent.absolute())
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
                                    background-color: rgb(37,39,43)
                                }
                        
                                QPushButton {
                                    border: none;
                                }
                                """)
        return button 

    def change_button_icon(self, short_path, size1, size2, button):
        current_directory = str(pathlib.Path(__file__).parent.parent.absolute())
        path = current_directory + short_path
        button_icon = QIcon()
        button_icon.addPixmap(QPixmap(path), QIcon.Normal, QIcon.Off)
        button.setIcon(button_icon)
        button.setIconSize(QSize(size1, size2))

    def initButtons(self):
        x_coord = 1420
        
        x_coord = x_coord-45
        self.minus_button = self.create_button(20, 20, 20, 5, x_coord, 12.5, '/icons/minus', self.minus_button_clicked)
       
        x_coord = x_coord-30
        self.plus_button = self.create_button(20, 20, 20, 20, x_coord, 12.5, '/icons/plus', self.plus_button_clicked)

        x_coord = x_coord-158
        current_directory = str(pathlib.Path(__file__).parent.parent.absolute())
        path = current_directory + '/icons/Columns'
        Columns_text_pic = QPixmap(path)
        Columns_text = QLabel(self)
        Columns_text.resize(148, 21)
        Columns_text.move(x_coord, 12)
        Columns_text.setPixmap(Columns_text_pic)


    def plus_button_clicked(self):
        self.change_button_icon('/icons/plus', 10, 10, self.plus_button)
        QApplication.processEvents()
        time.sleep(0.05)

        #print(self.table.columnCount())
        length = self.table.columnCount()
        self.table.insertColumn(length)
        #print(self.table.columnCount())

        Font = QFont("Roboto",12)
        Font.setBold(True)

        self.table.setHorizontalHeaderItem(length, QTableWidgetItem('Q'+str(length+1)))
        self.table.horizontalHeaderItem(length).setFont(Font)

        for row in range(0, self.table.rowCount()):
            self.table.setItem(row, length, QTableWidgetItem(''))
            self.table.item(row, length).setTextAlignment(Qt.AlignCenter)
            self.table.item(row, length).setFont(Font)

        self.machine.amount_of_states += 1
        self.machine.table[str(self.machine.amount_of_states)] = {}

        self.change_button_icon('/icons/plus', 20, 20, self.plus_button)
        return
    
    def minus_button_clicked(self):
        self.change_button_icon('/icons/minus', 10, 2.5, self.minus_button)
        QApplication.processEvents()

        self.machine.amount_of_states -= 1
        self.machine.table.pop(str(self.table.columnCount()))
        self.table.removeColumn(self.table.columnCount()-1)
        time.sleep(0.05)
        


        self.change_button_icon('/icons/minus', 20, 5, self.minus_button)
        return


    ####################################################################################################################
    #                                                       Table                                                      #
    ####################################################################################################################
    
    def initTable(self, rows = 0, columns = 13):
        self.table = QTableWidget(rows, columns, self)
        self.table.resize(1360, 695)
        self.table.move(40, 50)
        
        self.table.setStyleSheet("""
        QTableWidget
        {
            border: 2px solid #2D2D2D;
            background-color: #252526;
        }

        QTableWidget::item
        {
            background-color: #FFFFFF;
            color: black;
        }

        QLineEdit { 
            background: #A5EFFF;
            color: #000000; 
            font: 12pt "Roboto";
            font: bold;
            qproperty-alignment: AlignCenter;
        }

        QTableWidget::item::hover:!selected
        {
            background-color: #E9FBFF;
        }

        QTableWidget::item::hover:selected
        {
            background-color: #A5EFFF;
        }

        QTableWidget QHeaderView:section
        {
            background-color: #252526;            
        }
        
        """)
        self.table.horizontalHeader().setStyleSheet("background-color:#252526; border-color: white;")
        self.table.verticalHeader().setStyleSheet("background-color:#252526;")

        self.table.verticalHeader().setDefaultAlignment(Qt.AlignCenter)

        Font = QFont("Roboto",12)
        Font.setBold(True)

        for column in range(1, self.table.columnCount()+1):
            self.table.setHorizontalHeaderItem(column-1, QTableWidgetItem('Q'+str(column)))
            self.table.horizontalHeaderItem(column-1).setFont(Font)

        for row in range(0, self.table.rowCount()):
            self.table.setVerticalHeaderItem(row, QTableWidgetItem(str(self.machine.alphabet[row])))
            self.table.verticalHeaderItem(row).setFont(QFont(Font))
            if self.machine.alphabet[row] == ' ':
                item = QTableWidgetItem('     λ    ')
                temp_font = QFont("Bruno Ace",12)
                temp_font.setBold(True)
                item.setFont(temp_font)
                self.table.setVerticalHeaderItem(row, item)

        
        self.table.itemChanged.connect(self.itemChanged)
        for column in range(0, self.table.columnCount()):
            for row in range(0, self.table.rowCount()):
                self.table.setItem(row, column, QTableWidgetItem(''))
                #self.table.item(row, column).setBackground(QColor(0,0,0))
                #self.table.item(row, column).setForeground(QColor(0,0,0))
                self.table.item(row, column).setTextAlignment(Qt.AlignCenter)
                self.table.item(row, column).setFont(Font)

        return 

    

    def itemChanged(self, item):
        if self.text_change_again:
            #print("Does not change")
            self.text_change_again = False
            return
        #print(item.text())
        state = str(item.column()+1)
        symbol = self.machine.alphabet[item.row()]
        command = item.text()

        if len(command) == 0:
            self.machine.delete_command(state, symbol)
            return

        if len(command) >= 2: 
            if '<' == command[0] and ('<' == command[1] or '.' == command[1] or '>' == command[1]): 
                command = split(command)
                command[0] = "\u034A"
                command = "".join(command)
            elif '>' == command[0] and ('<' == command[1] or '.' == command[1] or '>' == command[1]): 
                command = split(command)
                command[0] = "\u034B"
                command = "".join(command)
            elif '.' == command[0] and ('<' == command[1] or '.' == command[1] or '>' == command[1]): 
                command = split(command)
                command[0] = "\u034C"
                command = "".join(command)

        if '<' in command: 
            command = command.split('<')
            goto = '<'
        elif '>' in command:
            command = command.split('>')
            goto = '>'
        elif '.' in command:
            command = command.split('.')
            goto = '.'
        else:
            self.call_warning_box("Немає інформації щодо переходу в інший стан"+'!')
            self.machine.delete_command(state, symbol)
            self.text_change_again = True
            item.setText('a') 
            self.text_change_again = True
            item.setText('')
            return
            

        if command[0] == '' and command[1] == '':
            command = symbol+goto+state
        elif command[0] == '':
            command = symbol+goto+command[1]               
        elif command[1] == '':
            command = command[0]+goto+state
        else:
            command = command[0]+goto+command[1]
         
        result = self.machine.replace_command(state, symbol, command)
       
        #print(result)
        if result == 0:  
            if ' ' == command[0]:
                command = list(command)
                command[0] = "λ"
                command = "".join(command)
                self.text_change_again = True
                item.setText('a') 
                self.text_change_again = True
                item.setText(command)
            else:
                if command[0] == "\u034A":
                    command = list(command)
                    command[0] = '<'
                    command = "".join(command)  
                elif command[0] == "\u034B":
                    command = list(command)
                    command[0] = '>'
                    command = "".join(command)
                elif command[0] == "\u034C":
                    command = list(command)
                    command[0] = '.'
                    command = "".join(command)
                self.text_change_again = True
                item.setText('a') 
                self.text_change_again = True
                item.setText(command)

            return
        
        else:
            if len(result) == 2:
                if result[0] == "У абетці немає символу":
                    self.call_warning_box(result[0]+' «'+str(result[1])+'»!')
                    self.machine.delete_command(state, symbol)
                    self.text_change_again = True
                    item.setText('a') 
                    self.text_change_again = True
                    item.setText('')
                else:
                    self.call_warning_box(result[0]+' Q'+str(result[1])+'!')
                    self.machine.delete_command(state, symbol)
                    self.text_change_again = True
                    item.setText('a') 
                    self.text_change_again = True
                    item.setText('')
                    
            else:
                self.call_warning_box(result+'!')
                self.machine.delete_command(state, symbol)
                self.text_change_again = True
                item.setText('a') 
                self.text_change_again = True
                item.setText('')


    def updateTable_items(self):
        Font = QFont("Roboto",12)
        Font.setBold(True)
        #print("updateTable_items")
        #print(self.machine.table)

        for column in range(0, self.table.columnCount()):
           for row in range(0, self.table.rowCount()):
               item_text = copy.copy(self.machine.command_getter(column+1, self.machine.alphabet[row]))
               if item_text != '':
                   if item_text[0] == ' ':
                       item_text[0] = 'λ'
               item_text = ("").join(item_text)
               
               self.text_change_again = True
               self.table.setItem(row, column, QTableWidgetItem(item_text))
               self.text_change_again = True
               self.table.item(row, column).setTextAlignment(Qt.AlignCenter)
               self.text_change_again = True
               self.table.item(row, column).setFont(Font)
        #print("updateTable_items end")
        return
        
    def updateTable_rows(self):
        if len(self.machine.alphabet) == self.table.rowCount():
            pass

        elif len(self.machine.alphabet) >= self.table.rowCount()+1:
            while(self.table.rowCount() <= len(self.machine.alphabet)-1):
                self.table.insertRow(self.table.rowCount())

        else:
            while(self.table.rowCount() >= len(self.machine.alphabet)+1):
                self.table.removeRow(self.table.rowCount()-1)
                

        Font = QFont("Roboto",12)
        Font.setBold(True)

        for row in range(0, self.table.rowCount()):
            self.table.setVerticalHeaderItem(row, QTableWidgetItem(str(self.machine.alphabet[row])))
            self.table.verticalHeaderItem(row).setFont(QFont(Font))
            if self.machine.alphabet[row] == ' ':
                item = QTableWidgetItem('     λ    ')
                temp_font = QFont("Bruno Ace",12)
                temp_font.setBold(True)
                item.setFont(temp_font)
                self.table.setVerticalHeaderItem(row, item)

        return
    
    def updateTable_columns(self):
        if self.machine.amount_of_states == self.table.columnCount():
            pass

        elif self.machine.amount_of_states >= self.table.columnCount()+1:
            while(self.table.columnCount() <= self.machine.amount_of_states-1):
                self.table.insertColumn(self.table.columnCount())

        else:
            while(self.table.columnCount() >= self.machine.amount_of_states+1):
                self.table.removeColumn(self.table.columnCount()-1)
                

        Font = QFont("Roboto",12)
        Font.setBold(True)

        for column in range(1, self.table.columnCount()+1):
            self.table.setHorizontalHeaderItem(column-1, QTableWidgetItem('Q'+str(column)))
            self.table.horizontalHeaderItem(column-1).setFont(Font)
        
        return


    def updateTable(self):
        self.updateTable_columns()
        self.updateTable_rows()
        self.updateTable_items()
        return

        
###############################################################################################
    def call_warning_box(self, message):
        current_directory = str(pathlib.Path(__file__).parent.parent.absolute())
        path = current_directory + '/icons/warning'
        messagebox = QMessageBox(QMessageBox.Warning, "Error", message, QMessageBox.Ok, parent=self)
        messagebox.setIconPixmap(QPixmap(path))
        messagebox.setFont(QFont("Bruno Ace",14))
        exe = messagebox.exec_()
            
       
    
