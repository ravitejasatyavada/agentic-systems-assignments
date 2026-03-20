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
