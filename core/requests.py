from pydantic import BaseModel
from typing import Optional

from core.models import *

class UserCreateRequest(BaseModel):
  email:str
  
