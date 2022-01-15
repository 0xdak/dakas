from dataclasses import dataclass
from datetime import date
from optparse import Option
from typing import Generic, TypeVar
from pydantic.generics import GenericModel
from core.models import *

T = TypeVar('T')
class BaseResponse(GenericModel, Generic[T]):
  info    : Info
  payload : T


class UserResponse(BaseModel):
  # TODO userId      : str
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





