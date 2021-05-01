class Turing_machine():
    def __init__(self, q_n=19, alphabet=[' ']):
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

    ##command functions
    def replace_command(self, state, symbol, command):
        #Перевіряємо чи існує такий стан у таблиці
        state = str(state)
        if not state in self.table:
            print("У таблиці немає cтану", state)
            return 1

        #Перевіряємо чи існує такий символ у абетці
        symbol = str(symbol)
        if not symbol in self.alphabet:
            print("У абетці немає символу", symbol)
            return 1

        command = str(command) 
        if '<' in command:
            command = command.split('<')

            if not command[0] in self.alphabet:
                print("У абетці немає символу", command[0])
                return 1
            
            if not command[1] in self.table:
                print("У таблиці немає cтану", command[1])
                return 1
            
            command.append(command[1])
            command[1] = '<'
            self.table[state][symbol] = command

        elif '>' in command:
            command = command.split('>')

            if not command[0] in self.alphabet:
                print("У абетці немає символу", command[0])
                return 1
            
            if not command[1] in self.table:
                print("У таблиці немає cтану", command[1])
                return 1
            
            command.append(command[1])
            command[1] = '>'
            self.table[state][symbol] = command

        elif '.' in command:
            command = command.split('.')

            if not command[0] in self.alphabet:
                print("У абетці немає символу", command[0])
                return 1
            
            if not command[1] in self.table:
                print("У таблиці немає cтану", command[1])
                return 1
            
            command.append(command[1])
            command[1] = '.'
            self.table[state][symbol] = command

        else:
            print("Немає інформації щодо переходу в інший стан")
            return 1
        





