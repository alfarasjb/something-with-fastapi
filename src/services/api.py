from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import logging
from pydantic import BaseModel


class ChatOpenAIPrompt(BaseModel):
    prompt: str


app = FastAPI()

logger = logging.getLogger(__name__)


@app.get("/")
def default_route(request: Request):
    try:
        print(request.query_params)
        return JSONResponse(status_code=200, content={"message": "Hello!"})
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")


@app.post("/chat", response_model=ChatOpenAIPrompt)
def chat_openai(request: Request, prompt: ChatOpenAIPrompt):
    # Put prompt in body
    try:
        prompt = prompt.prompt
        logger.info(f"Chat OpenAI. Request: {prompt}")
        return JSONResponse(status_code=200, content={"message": "Chat OpenAI"})
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
