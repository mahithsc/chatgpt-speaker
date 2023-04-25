import whisper

class STT:
    def __init__(self):
        self.model = whisper.load_model("base")
        
    def transcribe(self, file_name):
        print("BEGIN TRANSCRIBE")
        self.result = self.model.transcribe(file_name)
        print("END TRANSCRIBE")
        return self.result["text"]