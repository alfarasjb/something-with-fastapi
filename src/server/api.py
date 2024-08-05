from fastapi import FastAPI
from src.server.routes import health, tests, api

""" 
Router prefix 
"""
HEALTH = "/health"
TESTS = "/tests"
API = "/api"

app = FastAPI()
app.include_router(health.health_router, prefix=HEALTH)
app.include_router(tests.tests_router, prefix=TESTS)
app.include_router(api.api, prefix=API)


