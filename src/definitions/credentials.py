from dotenv import load_dotenv
import os

load_dotenv()


class Credentials:
    @classmethod
    def openai_api_key(cls) -> str:
        return os.getenv("OPENAI_API_key")

    @classmethod
    def db_username(cls) -> str:
        return os.getenv("DB_USERNAME", "postgres")

    @classmethod
    def db_password(cls) -> str:
        return os.getenv("DB_PASSWORD", "admin")


class EnvVariables:
    @classmethod
    def chat_model(cls) -> str:
        return os.getenv("CHAT_MODEL", "gpt-3.5-turbo")

    @classmethod
    def db_host(cls) -> str:
        return os.getenv("DB_HOST", "localhost")

    @classmethod
    def db_port(cls) -> str:
        return os.getenv("DB_PORT", "5432")

    @classmethod
    def db_name(cls) -> str:
        return os.getenv("DB_NAME", "TestDB")