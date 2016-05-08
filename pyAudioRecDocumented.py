import pyaudio
import wave
 
FORMAT = pyaudio.paInt16 #sample size is This FORMAT
#16 bits in the format
CHANNELS = 2# 2 = stereo, 1 = mono.
RATE = 44100 #We're sampling 44100 samples/sec
#Audio Rate =~ Frame Rate in Videos
CHUNK = 1024 #data is divided up into chunks. It's easier to process this way.
             #it's like a buffer. A continuous stream would be difficult to process
             #and take up all of the resources.
RECORD_SECONDS = 5 #this is the duration that we will record in seconds
WAVE_OUTPUT_FILENAME = "file.wav" #this is the name of the audio wave file
                                  #that we will output with the recording.
 
audio = pyaudio.PyAudio()#instantiation of pyaudio.
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,#sample size is the format
                rate=RATE, input=True,#rate at which samples are taken.input
                                      #has to equal True, or it wont run, or
                                      #record.
                frames_per_buffer=CHUNK)
print "recording..."
frames = [] #array frames, to capture the audio data recorded.


#for loop that captures the audio data in chunks that is being recorded.
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):#No idea why the equation
                                                      #is used.
    data = stream.read(CHUNK)#sets the chunk of audio data to 'data'
    frames.append(data)#adds the chunk of data to frames.
print "finished recording"
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

#transfers the data captured and the parameters to the wavefile
#and then closes it.
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
