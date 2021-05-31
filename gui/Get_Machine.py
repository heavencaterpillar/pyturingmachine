from Decoder import Decoder
import pathlib
def Get_Machine():
    current_directory = str(pathlib.Path(__file__).parent.absolute().parents[0])
    path = current_directory + '/input/input'
    f = open(path)

    New_decoder = Decoder()
    Decoded_MT = New_decoder.Dikarev_decoder(f)
    return Decoded_MT




