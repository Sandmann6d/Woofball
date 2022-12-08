# import pgzero
# from pygame import mixer
# from pgzero import music

import librosa
import sounddevice as sd
import threading
import time
import pyaudio

p = pyaudio.PyAudio()
p2 = pyaudio.PyAudio()

import pyaudio
import wave

class AudioFile:
    chunk = 1024

    def __init__(self, file):
        """ Init audio stream """ 
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()

# Usage example for pyaudio
a = AudioFile("music/themewav.wav")
a2 = AudioFile("sounds/goal0.wav")

def play_thread(x: AudioFile):
    x.play()
    x.close()

t = threading.Thread(target=play_thread, daemon=True, args=(a,))
t2 = threading.Thread(target=play_thread, daemon=True, args=(a2,))

t.start()
#t2.join()
time.sleep(5)
t2.start()
#t2.join()
time.sleep(5)

# def p(file):
#     sd.play(file, 22050)

# f, sr = librosa.load('music/themewav.wav')
# f1, sr = librosa.load('sounds/goal0.wav')
# sd.play(f, sr)
# time.sleep(10)

# t = threading.Thread(target=p, daemon=True, args=(f1,))
# t.start()
# time.sleep(2)
# sd.stop()