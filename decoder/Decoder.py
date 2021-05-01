from Turing_machine import Turing_machine

class Decoder():
    def __init__(self):
        return None

    def Dikarev_decoder(self, file):

        file_list = file.read()
        file_list = file_list.split('\n')
        file_list.pop(0)
        file_list.pop()
        max_state = 0
        alphabet = [' ']

        #Чистим данные, ищем самое большое состояние и наполняем алфавит
        for i in range(len(file_list)):
            line = file_list[i]
            line = line.split(' ')
            

            if line[1] == '':
                line[0] = ' '    
                line.pop(1)
            elif not line[0] in alphabet:
                alphabet.append(line[0])  
        
                
            temp = line[1].split('q')

            if '!' in temp[1]:
                line[1] = temp[1].split(':')[0]
                line.append('0') 
                ##Ищем самое большое состояние    
                max_state_in_line = int(line[1])

            else:    
                line[1] = temp[1].split(':')[0]
                line.append(temp[2])
                ##Ищем самое большое состояние
                max_state_in_line = max(int(line[1]), int(temp[2]))

            max_state = max(max_state_in_line, max_state)

            if line[2] == '':
                line[2] = ' '
                line.pop(3)

            if line[3] == 'R':
                line[3] = '>'
            elif line[3] == 'L':
                line[3] = '<'
            elif line[3] == 'S':
                line[3] = '.'
            #print(line)

            if not line[2] in alphabet:
                alphabet.append(line[2]) 

            file_list[i] = line 
        
        #Получили строчки в файле в виде ['Символ1', 'Состояние1', 'Символ2', 'Направление', 'Состояние2']
        Encoded_MT = Turing_machine(max_state, alphabet)
        for line in file_list:
            Encoded_MT.replace_command(line[1], line[0], line[2]+line[3]+line[4]) 

        return Encoded_MT

#    def Dikarev_encoder(self, MT):
        
#        for symbol in MT.alphabet

