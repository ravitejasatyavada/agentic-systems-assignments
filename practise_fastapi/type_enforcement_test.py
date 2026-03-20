# def type_enforcement_test(cls, roll: int, name: str):
#     return roll, name
#
# print(type_enforcement_test(100, "ravi"))
# print(type_enforcement_test("101", "ravi"))
# print(type_enforcement_test(102, 103))
# print(type_enforcement_test("ravi", 103))


from pydantic import BaseModel, Field
from typing import Dict


class TypeEnforcementTest(BaseModel):
    id: int = Field(ge=100, le=500)
    name: str = Field(max_length=50)
    parents_contact: Dict[str, int]


students = {"id": 100, "name": "ravi"}
student = TypeEnforcementTest(**students)
print(student.id)

students = {"id": "100", "name": "ravi"}
student = TypeEnforcementTest(**students)
print(student.id)


# students = {"id": "Ravi", "name": 100}
# student = TypeEnforcementTest(**students)
# print(student.id)

students = {"id": 100, "name": "Raviteja", "parents_contact": {"father": 12345, "mother": 67890}}
student = TypeEnforcementTest(**students)
print(student.parents_contact)

"""
Exception throwing -- 
Traceback (most recent call last):
  File "/Users/tejasahiti/PycharmProjects/agentic-systems-assignments/practise_fastapi/type_enforcement_test.py", line 21, in <module>
    student = TypeEnforcementTest(**students)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pydantic/main.py", line 214, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for TypeEnforcementTest
parents_contact
  Field required [type=missing, input_value={'id': 100, 'name': 'ravi'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.10/v/missing
"""