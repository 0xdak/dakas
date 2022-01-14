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

# @dataclass
class UserResponse(BaseModel):
  # userId      : str
  email       : str = None
  # isActive    : bool = False
  # createdDate : str  = None
  class Config:
    orm_mode = True

  # # converting User to UserResponse class to show to user...
  # # User --> UserResponse
  # def __init__(self, user: User) -> User:
  #   self.email       = user.email
  #   self.password    = user.password
  #   self.firstname   = user.firstname
  #   self.lastname    = user.lastname
  #   self.about       = user.about
  #   self.isActive    = False
  #   self.createdDate = datetime.now  # TODO what is date format?
  #   # TODO uid



