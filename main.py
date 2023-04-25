from gpt_client import ChatGPTClient
from stt import SpeechToText
from gtts import gTTS
import os

# getting key from the file
with open('key.txt', 'r') as f:
    key = f.readline()

transcribe = SpeechToText()
chat_client = ChatGPTClient(key)

while True:
    text = transcribe.recognize_speech()

    if text:
        response = chat_client.send_message(text)
        print(response)

        myobj = gTTS(text=response, lang='en', slow=False)
  
        myobj.save("response.mp3")
        
        os.system("mpg123 response.mp3")