from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id_user: Optional[int] = None
    name : str
    date : str