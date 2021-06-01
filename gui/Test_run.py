from Turing_machine import Turing_machine 
from Turing_machine_emulator import Turing_machine_emulator 
from Decoder import Decoder
from Get_Machine import Get_Machine 

Machine = Get_Machine()

##################################
Emulator = Turing_machine_emulator(['|', '1', '0'])

Emulator.tape = {-13: ' ', -12: ' ', -11: ' ', -10: ' ', -9: ' ', -8: ' ', -7: ' ', -6: ' ', -5: ' ', -4: ' ', -3: ' ', -2: ' ', -1: '1', 0: '|', 1: '1', 2: '1', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' ', 10: ' ', 11: ' ', 12: ' ', 13: ' '}  

print(Emulator.tape)
emulate = 1
while (emulate == 1):
    
    emulate = Emulator.emulate_one_step(Machine)
