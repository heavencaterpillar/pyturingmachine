import pathlib, os, sys
sys.path.append("")

from machine.decoder import Decoder

def Get_Machine():
    current_directory = str(pathlib.Path(__file__).parent.absolute())
    path = current_directory + '/input/input'
    f = open(path)

    New_decoder = Decoder()
    Decoded_MT = New_decoder.Dikarev_decoder(f)
    return Decoded_MT
