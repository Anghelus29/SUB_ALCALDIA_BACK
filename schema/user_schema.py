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
    