from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class CustomExceptionSample(Exception):
    def __init__(self, reference):
        self.reference = reference


@app.exception_handler(CustomExceptionSample)
def custom_exception_definition(request: Request, exc: CustomExceptionSample):
    return JSONResponse(status_code=404,
                        content={"request_path": request.base_url.hostname,
                                 "message": exc.reference
                                 })


@app.get("/customexception")
def custom_exception_api():
    raise CustomExceptionSample(reference="sample")
