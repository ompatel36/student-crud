from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    id: int = 0
    name: str
    email: str
    course: str
    semester: int