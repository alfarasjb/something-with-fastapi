from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import logging
from src.utils.generic_responses import GenericResponses

health_router = APIRouter()

logger = logging.getLogger(__name__)


@health_router.get("/")
def default_route(request: Request) -> JSONResponse:
    """
    This is a health-check route.

    Tests the api connection
    """
    try:
        return GenericResponses.success()
    except Exception as e:
        logger.error(f"{request.url}. An unknown error occurred. Error: {e}")
        return GenericResponses.internal_server_error()
