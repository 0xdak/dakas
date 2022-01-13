from typing import Optional
from pydantic import BaseModel


class Info(BaseModel):
  success : Optional[bool] = None
  code    : Optional[int]  = None
  message : Optional[str]  = None
  

class User(BaseModel):
  username : Optional[str] = None
  email    : Optional[str] = None

