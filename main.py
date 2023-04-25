from speach_to_text import STT
from recorder import Recorder
import threading
import time

stt = STT()
recorder = Recorder()
transcribe_thread = threading.Thread(target=stt.transcribe)

start_time = time.time()
print("starts recording")
while time.time() - start_time < 5:
    recorder.capture_audio()
    transcribe_thread.join()

recorder.save()
recorder.close()
print("end recording")

print(stt.transcribe("recording.wav"))