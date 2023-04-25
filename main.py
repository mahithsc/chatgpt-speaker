from speach_to_text import STT
from recorder import Recorder
from gpt_client import ChatGPTClient

# getting key from the file
with open('key.txt', 'r') as f:
    key = f.readline()

chat_client = ChatGPTClient(key)

# stt = STT()
# recorder = Recorder()