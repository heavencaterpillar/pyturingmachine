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
            #self.__print()    
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

    def emulate_one_step(self, Turing_machine):
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
        return 1

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















