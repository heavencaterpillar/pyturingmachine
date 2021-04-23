from Turing_machine import Turing_machine 
from Decoder import Decoder 

class Turing_machine_emulator():
    def __init__(self, tape = [], position = 0, state = 1):
        self.tape = dict(enumerate(tape)) #лента эмулятора
        self.position = position #текущая позиция на ленте
        self.state = state #текущее состояние в МТ

    def __print(self):
        add = True
        counter = 0
        for position in self.tape:
            if position == self.position:
                add = False
            if add:
                counter += 1
            print(self.tape[position], end = '')
        print('')
        print(' '*counter, end = '')
        print('^')
        print('')


    def emulate(self, Turing_machine):
        while(True):
            self.__print()    
            command = Turing_machine.table[str(self.state)][str(self.tape[self.position])]
            self.tape[self.position] = command[0]

            if command[1] == '<':
                self.position -= 1
                try:
                    self.tape[self.position]
                except KeyError:
                    temp_dict = {self.position : ' '} #?????????????
                    temp_dict.update(self.tape)
                    self.tape = temp_dict       
            elif command[1] == '>':
                self.position += 1
                try:
                    self.tape[self.position]
                except KeyError:
                    self.tape[self.position] = ' '
            self.state = command[2]
            if self.state == '0':
                self.__print()
                return 0

    def __print_in_file(self):
        add = True
        counter = 0
        for position in self.tape:
            if position == self.position:
                add = False
            if add:
                counter += 1
            print(self.tape[position], end = '')
        print('')
        print(' '*counter, end = '')
        print('^')
        print('')


    def emulate_in_file(self, Turing_machine):
        while(True):
            self.__print()    
            command = Turing_machine.table[str(self.state)][str(self.tape[self.position])]
            self.tape[self.position] = command[0]

            if command[1] == '<':
                self.position -= 1
                try:
                    self.tape[self.position]
                except KeyError:
                    temp_dict = {self.position : ' '} #?????????????
                    temp_dict.update(self.tape)
                    self.tape = temp_dict       
            elif command[1] == '>':
                self.position += 1
                try:
                    self.tape[self.position]
                except KeyError:
                    self.tape[self.position] = ' '
            self.state = command[2]
            if self.state == '0':
                self.__print()
                return 0



















#MT
#MT = Turing_machine()

#MT.add_symbol('0')
#MT.add_symbol('1')
#MT.add_symbol('_')

#MT.replace_command(1, '0', '0>1')
#MT.replace_command(1, '1', '1>1')
#MT.replace_command(1, ' ', '_<2')
#MT.replace_command(2, '0', '0<2')
#T.replace_command(2, '1', '1<2')
#MT.replace_command(2, ' ', '_>0')

#print(MT.table)
#print(MT.alphabet)

#Emulator
#Emulator = Turing_machine_emulator(['1', '1', '0', '1'])
#Emulator.emulate(MT)

f = open('/home/anton/IASA/Kyrs_2/Semestr_2/OOP/Individual_work/Emulator/Decoder/input')

New_decoder = Decoder()
Decoded_MT = New_decoder.Dikarev_decoder(f)
########Вводить значения тут######
mylist = [char for char in "1111|11010010"]
##################################
Emulator = Turing_machine_emulator(['1', '1', '1', '1', '1', '|', '1', '1', '1', '1', '1', '0', '0'])
Emulator.emulate(Decoded_MT)
