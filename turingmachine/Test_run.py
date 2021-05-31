from Turing_machine import Turing_machine 
from Decoder import Decoder 
from Turing_machine_emulator import Turing_machine_emulator 


###################
Test = 2
if Test == 1:   
    MT = Turing_machine()   
    MT.add_symbol('0')
    MT.add_symbol('1')
    MT.add_symbol('_')  
    MT.replace_command(1, '0', '0>1')
    MT.replace_command(1, '1', '1>1')
    MT.replace_command(1, ' ', '_<2')
    MT.replace_command(2, '0', '0<2')
    MT.replace_command(2, '1', '1<2')
    MT.replace_command(2, ' ', '_>0')   
    print(MT.table)
    print(MT.alphabet)  
    Emulator = Turing_machine_emulator(['1', '1', '0', '1'])
    Emulator.emulate(MT)

if Test == 2:
    f = open('/home/anton/IASA/Kyrs_2/Semestr_2/OOP/Individual_work/Emulator/Decoder/input')

    New_decoder = Decoder()
    Decoded_MT = New_decoder.Dikarev_decoder(f)
    New_decoder.Dikarev_encoder(Decoded_MT)
    ########Вводить значения тут######
    mylist = [char for char in "101|11"]
    ##################################
    Emulator = Turing_machine_emulator(mylist)
    emulate = 1 
    while (emulate == 1):
            emulate = Emulator.emulate_one_step(Decoded_MT)


if Test == 3:
    print('Hello')
    f = open("/home/anton/IASA/Kyrs_2/Semestr_2/OOP/Individual_work/pyturingmachine/output/myfile.txt", "w")
    f.write("Woops! I have deleted the content!\n")
    f.write("Woops! I have deleted the content!")
    f.close()