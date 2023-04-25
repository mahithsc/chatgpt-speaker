import openai

class ChatGPTClient:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.messages = []

    # sends message and returns the response
    def send_message(self, message):
        
        self.messages.append(
            {"role": "user", "content": message}
        )

        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = self.messages
        )
        
        self.messages.append(completion.choices[0].message)
        return completion.choices[0].message
    
    # clears the messages from the messages list
    def clear_messages(self):
        self.messages = []