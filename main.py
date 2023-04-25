from speach_to_text import STT
from recorder import Recorder
from gpt_client import ChatGPTClient
from gtts import gTTS
import os


# # getting key from the file
# with open('key.txt', 'r') as f:
#     key = f.readline()

# chat_client = ChatGPTClient(key)

# mytext = chat_client.send_message("tell me anorther joke").content

# myobj = gTTS(text=mytext, lang='en', slow=False)
  
# myobj.save("response.mp3")
  
# os.system("mpg123 response.mp3")