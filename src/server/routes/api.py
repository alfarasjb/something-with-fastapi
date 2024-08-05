from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import logging
from src.utils.generic_responses import GenericResponses
from src.definitions import response_models


api = APIRouter()
logger = logging.getLogger(__name__)


@api.get("/")
def default_route(request: Request) -> JSONResponse:
    """
    `/api` test route
    """
    try:
        return GenericResponses.success()
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return GenericResponses.internal_server_error()


@api.post("/chat", response_model=response_models.ChatOpenAIPrompt)
def chat_openai(request: Request, chat_request: response_models.ChatOpenAIPrompt):
    """ 
    payload = {"prompt": <prompt> 
    """
    try:
        prompt = chat_request.prompt
        logger.info(f"Chat OpenAI. Request: {prompt}")
        return GenericResponses.success()
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return GenericResponses.internal_server_error()
