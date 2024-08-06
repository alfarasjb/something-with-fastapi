from typing import Callable
from fastapi import FastAPI, Request, Response

from src.database.database import SessionLocal
from src.server.routes import health, tests, api, db

""" 
Router prefix 
"""
HEALTH = "/health"
TESTS = "/tests"
API = "/api"
DB = "/db"

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next: Callable) -> Response:
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(health.health_router, prefix=HEALTH)
app.include_router(tests.tests_router, prefix=TESTS)
app.include_router(api.api, prefix=API)
app.include_router(db.db_router, prefix=DB)
