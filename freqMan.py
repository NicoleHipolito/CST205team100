import pyaudio
import sys
import numpy as np
import wave
import audioop
import struct

chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 41000
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                output = True,
                frames_per_buffer = chunk)

swidth = 2

print "* recording"



while(True):

    data = stream.read(chunk)
    data = np.array(wave.struct.unpack("%dh"%(len(data)/swidth), data))*2

    data = np.fft.rfft(data)
    #MANipulation
    data = np.fft.irfft(data)

    dataout = np.array(data*0.5, dtype='int16') #undo the *2 that was done at reading
    chunkout = struct.pack("%dh"%(len(dataout)), *list(dataout)) #convert back to 16-bit data
    stream.write(chunkout)
    print "* done"

    stream.stop_stream()
    stream.close()
    p.terminate()
