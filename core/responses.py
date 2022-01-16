from datetime import date
from typing import Generic, TypeVar
import uuid
from pydantic.generics import GenericModel
from core.models import *
from sqlalchemy.dialects.postgresql import UUID

T = TypeVar('T')
class BaseResponse(GenericModel, Generic[T]):
  info    : Info
  payload : T = None


class UserResponse(BaseModel):
  userId     : str = ""
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


