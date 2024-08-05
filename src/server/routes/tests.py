import logging

from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse

from src.definitions import response_models
from src.utils.generic_responses import GenericResponses

tests_router = APIRouter()

logger = logging.getLogger(__name__)

""" 
Endpoints 
"""
CHAT_REQUEST = "/chat-request"
CHAT_REQUEST_PYDANTIC = "/chat-request-pydantic"


@tests_router.post(CHAT_REQUEST)
async def chat_with_requests(request: Request):
    try:
        response_body = await request.json()
        prompt = response_body.get("prompt")
        logger.info(f"Prompt: {prompt}")
        return GenericResponses.success()
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return GenericResponses.internal_server_error()


@tests_router.post(CHAT_REQUEST_PYDANTIC, response_model=response_models.ChatOpenAIPrompt)
async def chat_with_pydantic(request: Request, chat_request: response_models.ChatOpenAIPrompt):
    """
    Uses pydantic for response model
    """
    try:
        prompt = chat_request.prompt
        logger.info(f"Chat OpenAI with Pydantic. Prompt: {prompt}")
        return GenericResponses.success()
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return GenericResponses.internal_server_error()
