from dotenv import load_dotenv
import os

load_dotenv()


class Credentials:
    @classmethod
    def openai_api_key(cls) -> str:
        return os.getenv("OPENAI_API_key")


class EnvVariables:
    @classmethod
    def chat_model(cls) -> str:
        return os.getenv("CHAT_MODEL", "gpt-3.5-turbo")
