from Decoder import Decoder
def Get_Machine():
    f = open('/home/anton/IASA/Kyrs_2/Semestr_2/OOP/Individual_work/Emulator/Decoder/input')

    New_decoder = Decoder()
    Decoded_MT = New_decoder.Dikarev_decoder(f)
    return Decoded_MT




