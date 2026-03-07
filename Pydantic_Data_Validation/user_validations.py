"""
Part 1: User Registration Validation
Create a Pydantic model UserRegister with:
username (str, min 5 characters)
email (valid email)
age (int, must be ≥ 18)
Validate incoming data and reject invalid inputs.
"""

from pydantic import BaseModel, Field, EmailStr


class UserRegister(BaseModel):
        username: str = Field(min_length=5, description="Minimum length of the field should be 5 characters")
        email: EmailStr
        age: int = Field(ge=18, description="validate the age must be 18 or more")


input1 = {"username": "raviteja", "email": "raviteja.satyavada@gmail.com", "age": 36}
ob1 = UserRegister(**input1)
print(ob1)

input1 = {"username": "ravi", "email": "raviteja.satyavada@com", "age": 10}
ob1 = UserRegister(**input1)
print(ob1)

