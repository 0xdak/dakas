from datetime import date, timedelta
from typing import Generic, TypeVar
from pydantic.generics import GenericModel
from core.models import *

T = TypeVar('T')
class BaseResponse(GenericModel, Generic[T]):
  info    : Info = None
  payload : T = None


class UserResponse(BaseModel):
  userId      : str = ""
  email       : str = ""
  firstname   : str = ""
  lastname    : str = ""
  about       : str = ""
  isActive    : bool = False
  createdDate : date  = None

  class Config:
    orm_mode = True
  # def __init__(self, user: User): # TODO maybe?
  #   self = self.from_orm(user)

class LoginResponse(BaseModel):
  access_token : str = ""
  tokenType    : str = ""
  userId       : str = ""
  tokenExpires : timedelta = None  # in seconds


