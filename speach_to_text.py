import whisper

class STT:
    def __init__(self):
        self.model = whisper.load_model("base")
        
    def transcribe(self):
        self.result = self.model.transcribe("test.mp3")
        return self.result["text"]