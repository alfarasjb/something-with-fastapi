"""
This is deprecated
"""

import logging

from fastapi import FastAPI, APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

from src.services import api_response_models as response_models
from src.services.chat import ChatModel
from src.utils.generic_responses import internal_server_error

app = FastAPI()
CHAT = ChatModel()

logger = logging.getLogger(__name__)
router = APIRouter()


@app.get("/")
def default_route(request: Request) -> JSONResponse:
    """
    Test route
    """
    try:
        print(request.query_params)
        return JSONResponse(status_code=200, content={"message": "Hello!"})
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return internal_server_error()


@app.post("/chat", response_model=response_models.ChatOpenAIPrompt)
def chat_openai(request: Request, prompt: response_models.ChatOpenAIPrompt) -> JSONResponse:
    """
    payload = {"prompt": <prompt>}
    """
    try:
        prompt = prompt.prompt
        logger.info(f"Chat OpenAI. Request: {prompt}")
        response = CHAT.chat(user_prompt=prompt)
        logger.info(f"OpenAI Response: {response}")
        return JSONResponse(status_code=200, content={"message": response})
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return internal_server_error()


@app.post("/chat-request")
async def chat_with_requests(request: Request):
    """
    Uses the request and checks payload instead of using pydantic response model
    """
    try:
        body = request.query_params
        response_body = await request.json()
        prompt = response_body.get("prompt")
        logger.info(f"Prompt: {prompt}")
        return JSONResponse(status_code=200, content={"message": "body"})
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return internal_server_error()


@router.post("/chat-request")
async def chat_with_requests_router(request: Request):
    try:
        response_body = await request.json()
        logger.info(f"Prompt: {response_body.get("prompt")}")
        return JSONResponse(status_code=200, content={"message": response_body.get("prompt")})
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return internal_server_error()

# Must put this at the end
app.include_router(router, prefix="/tests")