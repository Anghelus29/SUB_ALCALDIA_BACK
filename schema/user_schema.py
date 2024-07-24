from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: str
    last_name: str
    type_of_user: str
    post: str
    office: str
    user_name: str
    password: str
    
class AttendanceSchema(BaseModel):
    id: Optional[int] = None
    id_people: int
    hardware: str
    software: str
    description: str
    date: str
    hour: str
    state: str

class ReportSchema(BaseModel):
    id: Optional[int] = None
    id_attendance: int
    state: str
    date_review: str
    work_done: str
