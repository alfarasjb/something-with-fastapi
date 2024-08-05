import logging
from typing import Optional

import openai
from openai import OpenAI
from tenacity import retry, stop_after_attempt, retry_if_exception_type

from src.definitions.credentials import Credentials, EnvVariables
from src.utils.decorators import decreasing_wait
from src.services.prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class ChatModel:
    def __init__(self):
        self.chat_model = EnvVariables.chat_model()
        self.model = OpenAI(api_key=Credentials.openai_api_key())
        self.max_tokens = 4096
        self.system_prompt = SYSTEM_PROMPT

    @retry(stop=stop_after_attempt(5), retry=retry_if_exception_type(openai.RateLimitError), wait=decreasing_wait)
    def chat(self, user_prompt: str = "") -> Optional[str]:
        logger.info(f"User Prompt: {user_prompt}")
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
        logger.info(f"Response: {response_message}")
        return response_message
