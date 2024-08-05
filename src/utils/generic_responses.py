from fastapi.responses import JSONResponse


def internal_server_error() -> JSONResponse:
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})
