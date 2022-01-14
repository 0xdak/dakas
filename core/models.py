from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from core.requests import UserCreateRequest

from requests import *
from sqlalchemy import Column, String, Integer, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Info(BaseModel):
  success : Optional[bool] = None
  code    : Optional[int]  = None
  message : Optional[str]  = None
  

class User(Base):
  __tablename__ = 'users'
  id          = Column(Integer, primary_key=True)
  email       = Column(String)
  password    = Column(String)
  firstname   = Column(String)
  lastname    = Column(String)
  about       = Column(String)
  # isActive    = Column(Boolean)
  # createdDate = Column(String)

  # # converting UserCreateRequest to User class to save to database...
  # # UserCreateRequest --> User 
  # def __init__(self, userCreateRequest: UserCreateRequest) -> UserCreateRequest:
  #   self.email       = userCreateRequest.email
  #   self.password    = userCreateRequest.password
  #   self.firstname   = userCreateRequest.firstname
  #   self.lastname    = userCreateRequest.lastname
  #   self.about       = userCreateRequest.about
  #   self.isActive    = False

  # TODO user_id??
  

