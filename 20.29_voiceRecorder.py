# If you want to know how to make a voice recorder  using Python, this Tutorial is for you. In this tutorial, I will walk you through how to make a voice recordeer using Python.
# So, Let's start:
import sounddevice
from scipy.io.wavfile import write
def aryanvoice_recorder(seconds, file):
    print("Recording Strated")
    print("Recoring in progress...")
    print()
    rec_var = sounddevice.rec((seconds * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write(file, 44100, rec_var)
    print("Recording Completed Successfully")

aryanvoice_recorder(10, "recordsave.wav")