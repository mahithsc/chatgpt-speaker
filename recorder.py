import pyaudio
import wave
import os

class Recorder():
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        self.frames = []
    
    def capture_audio(self):
        data = self.stream.read(1024)
        self.frames.append(data)
    
    def save(self):
        sound_file = wave.open("recording.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(self.frames))
        self.frames = []
        sound_file.close()

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()