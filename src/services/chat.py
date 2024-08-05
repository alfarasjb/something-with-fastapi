from typing import Optional

from openai import OpenAI

from src.definitions.credentials import Credentials, EnvVariables


class ChatModel:
    def __init__(self):
        self.chat_model = EnvVariables.chat_model()
        self.model = OpenAI(api_key=Credentials.openai_api_key())
        self.max_tokens = 4096
        self.system_prompt = "You are a helpful assistant"

    def chat(self, user_prompt: str = "") -> Optional[str]:
        if not user_prompt:
            return
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        response = self.model.chat.completions.create(
            model=self.chat_model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=0.7
        )
        response_message = response.choices[0].message.content
        return response_message
