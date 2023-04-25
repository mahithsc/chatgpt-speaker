import speech_recognition as sr

class STT:
    def __init__(self):
        self.r = sr.Recognizer()
        self.source = sr.Microphone()
        self.r = self.r.adjust_for_ambient_noise(self.source)
    
    def listen(self):
        audio = self.r.listen(self.source)
        try:
            text = self.r.recognize_google(audio)
            print("You said: {}".format(text))
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
