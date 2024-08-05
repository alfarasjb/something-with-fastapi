from fastapi.responses import JSONResponse


class GenericResponses:
    @classmethod
    def internal_server_error(cls) -> JSONResponse:
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

    @classmethod
    def success(cls) -> JSONResponse:
        return JSONResponse(status_code=200, content={"message": "Success"})