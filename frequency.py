import pyaudio
import numpy as np
import wave
import stream
import struct
import math
import scipy
import wavfile

def freqManip():
    # length of data to read.
    chunk = 1199520
    # open the file for reading.
    nh = wave.open("GameSong.wav")
    nwidth = nh.getsampwidth()

    # create an audio object
    p = pyaudio.PyAudio()

    # open stream based on the wave object which has been input.
    stream = p.open(format =
                    p.get_format_from_width(nh.getsampwidth()),
                    channels = nh.getnchannels(),
                    rate = nh.getframerate(),
                    output = True)

    data = nh.readframes(chunk)

    #This is the loop that manipulates audio:
    while(True):
        print("Length of data:", len(data))
        print("Width: ", nwidth)
        print("l(d)/w: ", (len(data)/nwidth))
        print("(l(d)/w)*2: ", (len(data)/nwidth)*2)
        data = np.array(wave.struct.unpack("%dh"%(len(data)/nwidth), data))*2
        #print data
        data = np.fft.fft(data)
        #print data

        dcnt = 0
        for d in data:
            #data[dcnt] = (d.real**2 + d.imag**2)
            data[dcnt] = (d.real+d.imag)
            #data[dcnt] = (data[dcnt])**0.5
            #data[dcnt] += 2
            dcnt += 1

        if (np.iscomplexobj(d)):
            d = d + 0j

        data = np.fft.ifft(data)

        dataout = np.array(data.real, dtype='int16')
        chunkout = struct.pack("%dh"%(len(dataout.real)), *list(dataout.real))
        #%dh = see https://docs.python.org/2/library/stdtypes.html#string-formatting-operations under String Formatting Operations
        # writing to the stream is what *actually* plays the sound.
        #!!!!!!!!!!!---------------------------!!!!!!!!!!!!!!!
        #try this later:
        #data = nh.readframes(chunkout)
        wavfile.write("realPlusImag.wav", nh.getframerate()*2, dataout)
        stream.stop_stream()
        stream.close()
def slowSong():
    chunk = 599760
    # open the file for reading.
    nh = wave.open("GameSong.wav")
    nwidth = nh.getsampwidth()

    # create an audio object
    p = pyaudio.PyAudio()

    # open stream based on the wave object which has been input.
    stream = p.open(format =
                    p.get_format_from_width(nh.getsampwidth()),
                    channels = nh.getnchannels(),
                    rate = nh.getframerate(),
                    output = True)

    data = nh.readframes(chunk)
    data = np.array(wave.struct.unpack("%dh"%(len(data)/nwidth), data))*2
    data = np.array(data, dtype='int16')
    wavfile.write("slow.wav", nh.getframerate(), data)
    stream.close()
def fastSong():
    chunk = 599760
    # open the file for reading.
    nh = wave.open("GameSong.wav")
    nwidth = nh.getsampwidth()

    # create an audio object
    p = pyaudio.PyAudio()

    # open stream based on the wave object which has been input.
    stream = p.open(format =
                    p.get_format_from_width(nh.getsampwidth()),
                    channels = nh.getnchannels(),
                    rate = nh.getframerate(),
                    output = True)

    data = nh.readframes(chunk)
    data = np.array(wave.struct.unpack("%dh"%(len(data)/nwidth), data))*2
    data = np.array(data, dtype='int16')
    wavfile.write("fast.wav", nh.getframerate()*4, data)
    stream.close()

slowSong()
fastSong()
freqManip()

p.terminate()
