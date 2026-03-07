"""
Part 1: You are building a User Registration System for an e-commerce platform.
Design a Pydantic model system with the following requirements:

Address Model

city → string (minimum length 3)
pincode → string (must be exactly 6 digits)
User Model

user_id → integer
name → string
email → email string
age → integer (must be ≥ 18)
address → nested Address model
is_premium → optional boolean (default = False)
Assignment validation should be enabled
"""

from pydantic import BaseModel, Field, field_validator, EmailStr


class Address(BaseModel):
    city: str = Field(min_length=3)
    pincode: str = Field(max_length=6)

    @field_validator('pincode')
    @classmethod
    def pin_code_validator(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise Exception("Pincod must be 6 digits")


class User(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    is_premium: bool = Field(default=False)


address = {"city": "Bengaluru", "pincode": "560049"}
address_obj = Address(**address)
user = {"user_id": 1235, "name": "Raviteja", "email": "raviteja.satyavada@gmail.com", "age": 20, "address": address_obj}
user_obj = User(**user)
print(user_obj)

address = {"city": "Bengaluru", "pincode": "CR05UW"}
address_obj = Address(**address)
user = {"user_id": 1235, "name": "Raviteja", "email": "raviteja.satyavada@gmail.com", "age": 20, "address": address_obj}
user_obj = User(**user)
print(user_obj.address)