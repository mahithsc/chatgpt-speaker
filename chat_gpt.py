import openai

class ChatGPtClient:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.messages = []

    # sends message and returns the response
    def send_message(self):
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = self.messages
        )
        print(completion.choices[0].message)
        self.messages.append(completion.choices[0].message)
        return completion.choices[0].message
    
    # clears the messages from the messages list
    def clear_messages(self):
        self.messages = []