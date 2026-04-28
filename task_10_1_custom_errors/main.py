from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Custom Errors API")

items = {
    1: {"id": 1, "title": "First item"},
    2: {"id": 2, "title": "Second item"},
}


class ErrorResponse(BaseModel):
    error_code: str
    message: str


class CustomExceptionA(Exception):
    def __init__(self, message: str = "Age must be 18 or higher"):
        self.message = message
        self.status_code = 400
        self.error_code = "AGE_ERROR"


class CustomExceptionB(Exception):
    def __init__(self, message: str = "Resource not found"):
        self.message = message
        self.status_code = 404
        self.error_code = "RESOURCE_NOT_FOUND"


@app.exception_handler(CustomExceptionA)
def custom_exception_a_handler(request: Request, exc: CustomExceptionA):
    print(f"{request.method} {request.url} {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(error_code=exc.error_code, message=exc.message).model_dump(),
    )


@app.exception_handler(CustomExceptionB)
def custom_exception_b_handler(request: Request, exc: CustomExceptionB):
    print(f"{request.method} {request.url} {exc.message}")
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(error_code=exc.error_code, message=exc.message).model_dump(),
    )


@app.get("/check-age", responses={400: {"model": ErrorResponse}})
def check_age(age: int):
    if age < 18:
        raise CustomExceptionA()
    return {"message": "Age accepted"}


@app.get("/items/{item_id}", responses={404: {"model": ErrorResponse}})
def get_item(item_id: int):
    if item_id not in items:
        raise CustomExceptionB()
    return items[item_id]
