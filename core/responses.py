from optparse import Option
from typing import Generic, TypeVar
from pydantic.generics import GenericModel
from core.models import *

T = TypeVar('T')
class BaseResponse(GenericModel, Generic[T]):
  info    : Info
  payload : T

class UserResponse(BaseModel):
    userId    : Optional[str]  = None
    email     : Optional[str]  = None
    password  : Optional[str]  = None
    firstname : Optional[str]  = None
    lastname  : Optional[str]  = None
    about     : Optional[str]  = None
    isActive  : Optional[bool] = False

