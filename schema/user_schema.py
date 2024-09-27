from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    type_of_user: Optional[str] = None
    post: Optional[str] = None
    office: Optional[str] = None
    user_name: Optional[str] = None
    password: Optional[str] = None
    
class AttendanceSchema(BaseModel):
    id: Optional[int] = None
    id_people: Optional[int] = None 
    hardware: Optional[str] = None
    software: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    hour: Optional[str] = None
    state: Optional[str] = None

class ReportSchema(BaseModel):
    id: Optional[int] = None
    id_attendance: Optional[int] = None  
    date_review: Optional[str] = None
    work_done: Optional[str] = None

