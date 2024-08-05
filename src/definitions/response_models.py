from pydantic import BaseModel


class ChatOpenAIPrompt(BaseModel):
    prompt: str
