class Turing_machine():
    def __init__(self, q_n=13, alphabet=[' ']):
        self.table = {}
        for i in range(0,q_n+1): self.table[str(i)] = {}
        self.alphabet = alphabet
        self.amount_of_states = q_n

    #alphabet functions
    def add_symbol(self, symbol):
        self.alphabet.append(symbol)
        return 0

    def delete_symbol(self, symbol):
        self.alphabet.remove(symbol)
        for i in self.table:
            try:
                del self.table[i][symbol]
            except KeyError:
                pass
        print(self.table)
        return 0

    #table functions
    ##state functions
    def add_state(self):
        self.amount_of_states += 1
        self.table[str(self.amount_of_states)] = {}
        return 0

    def delete_state(self):
        self.amount_of_states -= 1
        self.table.pop(str(self.amount_of_states))
        return 0

    def delete_command(self, state, symbol):
        try:
            self.table[state][symbol]
        except KeyError:
            return
        del self.table[state][symbol]
        #print("delete_command")
        #print(self.table)
        return

    ##command functions
    def replace_command(self, state, symbol, command):
        #print("replace_command", state , symbol)
        #Перевіряємо чи існує такий стан у таблиці
        state = str(state)
        if not state in self.table:
            #print("У таблиці немає cтану", state)
            return "У таблиці немає cтану", state

        #Перевіряємо чи існує такий символ у абетці
        symbol = str(symbol)
        if not symbol in self.alphabet:
            #print("У абетці немає символу", symbol)
            return "У абетці немає символу", symbol

        command = str(command)
        if '<' in command:
            command = command.split('<')
            if command[0] == "\u034A":
                command[0] = '<'
            elif command[0] == "\u034B":
                command[0] = '>'
            elif command[0] == "\u034C":
                command[0] = '.' 
            #print(command)

            if not command[0] in self.alphabet:
                if command[0] == '':
                    command[0] = symbol
                else:
                    #print("У абетці немає символу", command[0])
                    return "У абетці немає символу", command[0]

            if not command[1] in self.table:
                #print("У таблиці немає cтану", command[1])
                return "У таблиці немає cтану", command[1]

            command.append(command[1])
            command[1] = '<'
            self.table[state][symbol] = command

        elif '>' in command:
            command = command.split('>')
            if command[0] == "\u034A":
                command[0] = '<'
            elif command[0] == "\u034B":
                command[0] = '>'
            elif command[0] == "\u034C":
                command[0] = '.' 

            if not command[0] in self.alphabet:
                if command[0] == '':
                    command[0] = symbol
                else:
                    #print("У абетці немає символу", command[0])
                    return "У абетці немає символу", command[0]

            if not command[1] in self.table:
                #print("У таблиці немає cтану", command[1])
                return "У таблиці немає cтану", command[1]

            command.append(command[1])
            command[1] = '>'
            self.table[state][symbol] = command

        elif '.' in command:
            command = command.split('.')
            if command[0] == "\u034A":
                command[0] = '<'
            elif command[0] == "\u034B":
                command[0] = '>'
            elif command[0] == "\u034C":
                command[0] = '.' 

            if not command[0] in self.alphabet:
                if command[0] == '':
                    command[0] = symbol
                else:
                    #print("У абетці немає символу", command[0])
                    return "У абетці немає символу", command[0]

            if not command[1] in self.table:
                #print("У таблиці немає cтану", command[1])
                return "У таблиці немає cтану", command[1]

            command.append(command[1])
            command[1] = '.'
            self.table[state][symbol] = command

        else:
            #print("Немає інформації щодо переходу в інший стан")
            return "Немає інформації щодо переходу в інший стан"
        
        #print(self.table)
        return 0

    def delete_symbol(self, symbol):
        #print("delete_symbol", symbol)
        self.alphabet.remove(symbol)
        for key in self.table:
            try:
                del self.table[key][symbol]
            except KeyError:
                pass
    
    def command_getter(self, state, symbol):
        try:
            #print(self.table[str(state)][symbol])
            return self.table[str(state)][symbol]
        except KeyError:
            return ''


#########################################################################
#                              Emulator                                 #
#########################################################################

class Turing_machine_emulator():

    def __init__(self, position = 0, state = 1, tape = [" "]*27):
        self.tape = dict() #лента эмулятора
        for i in range(-13, len(tape) // 2 + 1):
            self.tape[i] = tape[i+13]
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
                #self.__print()
                return 0

    def emulate_one_step(self, Turing_machine):
        #self.__print()
        try:
            command = Turing_machine.table[str(self.state)][str(self.tape[self.position])]
        except KeyError:
            return self.state, self.tape[self.position]
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
