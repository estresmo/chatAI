import os
import openai

class chatAI:
    def __init__(self, api_key:str, org:str) -> None:
        openai.organization = org
        openai.api_key = api_key

    def sendMessage(self, message: str):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": message}]
        )
        return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    org = "org-2t6czCfX79NXhNdPvPzLZauZ"
    api_key = os.getenv("OPENAI_API_KEY")
    chat = chatAI(api_key, org)
    print(chat.sendMessage("Hola mi amigo"))
