from pydantic import BaseModel
from typing import Optional

from core.models import *

class UserCreateRequest(BaseModel):
  email       : Optional[str] = None
  password    : Optional[str] = None
  firstname   : Optional[str] = None
  lastname    : Optional[str] = None
  about       : Optional[str] = None
  
  def __init__(self, user):
    self.email     = user.email
    self.password  = user.password
    self.firstname = user.firstname
    self.lastname  = user.lastname
    self.about     = user.about
