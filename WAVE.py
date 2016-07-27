import numpy as np
import random
import struct

class WAVE(object):
    
    def __init__(self):
        # define header
        RIFF_HEADER = b"\x52\x49\x46\x46"   # "RIFF"
        FILE_SIZE = b"\xAA\xAA\00\00"       # tekitou
        WAVE_HEADER = b"\x57\x41\x56\x45"   # "WAVE"
        WAVE_FORMAT = b"\x66\x6D\x74\x20"   # "fmt "
        FORMAT_SIZE = b"\x10\x00\x00\x00"   # 16
        FORMAT_ID = b"\x01\x00"             # linearPCM
        CHUNNELS = b"\x01\x00"              # mono
        SAMPLING_RATE = b"\x44\xAC\x00\x00" # 44100
        BYTES_PER_SEC = b"\x88\x58\x01\x00" # 44100 * 2(16bit) * 1(mono)
        BLOCK_SIZE = b"\x02\x00"            # 2(16bit) * 1(mono)
        SIGNIFICANT = b"\x10\x00"           # 16bit
        DATA_HEADER = b"\x64\x61\x74\x61"   # "data"
        DATA_SIZE = b"\xAA\xAA\x00\x00"     # tekitou

        self.HEADER = RIFF_HEADER + FILE_SIZE + WAVE_HEADER + WAVE_FORMAT + FORMAT_SIZE + FORMAT_ID + CHUNNELS + SAMPLING_RATE + BYTES_PER_SEC + BLOCK_SIZE + SIGNIFICANT + DATA_HEADER + DATA_SIZE

    def make_wave(self, A=32767.0, fs=44100, f0_orig=262, rand=False, filter_range=[20, 15000]):
        
        def f0():
            # convert f0_orig to new f0
            if rand:
                return random.randint(filter_range[0], filter_range[1])
            
            return f0_orig
            
        # make wave
        wave = []

        for n in range(fs):
            f = A*np.sin(2*np.pi*f0()*n/fs)
            wave.append(int(f))
            
        return wave

    def wave_to_binary(self, wave):
        # convert wave to binary data
        binary =  struct.pack("h" * len(wave), *wave)
        
        return binary

    def write(self, binary):
        # output file
        res = self.HEADER + binary
        with open("output_do.wav", "wb") as f:
            f.write(res)
        
    def executor(self, rand=False, filter_range=[20, 15000]):
        wave = self.make_wave(rand=rand, filter_range=filter_range)
        binary = self.wave_to_binary(wave)
        self.write(binary)
        
if __name__ == "__main__":
    w = WAVE()
    w.executor(rand=True, filter_range=[20, 25])