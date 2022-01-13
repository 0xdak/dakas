from pydantic import BaseModel
from typing import Optional

class UserCreateRequest(BaseModel):
  email       : Optional[str] = None
  password    : Optional[str] = None
  firstname   : Optional[str] = None
  lastname    : Optional[str] = None
  about       : Optional[str] = None
  
