"""
pip install fastapi uvicorn
uvicorn main:app --reload

--
Test the API using a browser or Postman, or curl:

Access /hello and verify that it returns the expected response.
Try accessing an undefined route (for example /unknown) and verify that the custom 404 exception handler response is returned.
Check the terminal logs to confirm that the middleware logs the request method and path.
--
Problem Statement
Middleware and Exception Handling in FastAPI
You are building a FastAPI application that logs every incoming request.

First, create a simple API endpoint /hello that returns the following JSON response:

{
  "message": "Hello, Welcome to FastAPI!"
}
Next, create a middleware that:

Logs the HTTP method (GET, POST, etc.)
Logs the URL path of the request
Prints a message before the request is processed
Prints a message after the response is returned
Finally, implement a simple exception handler for 404 Not Found errors. This handler should return a custom JSON message when a user tries to access a route that is not defined in the application (for example, /unknown).

Example response for an undefined route:

{
  "message": "The requested resource was not found"
}

"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.middleware("http")
async def middleware_component(request: Request, call_next):
    print("Welcome to Middleware component")
    print(f"Incoming API method {request.method}")
    url_path = request.url
    request_path = url_path.path
    print(f"Incoming API base URL {url_path}")
    print(f"Passing on to {type(str(request_path))}")
    if str(request_path) != "/hello":
        print("Inside exception")
        return JSONResponse(status_code=404, content={"message": "The requested resource was not found"})
    print(f"Passing on to {request_path}")
    response = await call_next(request)
    print(f"Response on to {request_path}")
    return response


@app.get("/hello")
async def hello_api():
    print("Hello from hello")
    return {"message": "Hello, Welcome to FastAPI!"}
