"""
Query Parameters
Requirement:
Create fastapi-and-databases GET endpoint /search that accepts two optional query parameters:

name (string)
age (integer)
Return the received parameters as JSON.
"""

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/search")
def search_method(name: str = Query(default="raviteja", description="Name parameter of the input"),
                  age: int = Query(default=36, description="Age parameter of the input")
                  ):
    return {"name": name, "age": age}

