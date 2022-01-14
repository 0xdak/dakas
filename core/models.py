from dataclasses import dataclass
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
  email       = Column(String, nullable=False)
  password    = Column(String, nullable=False)
  firstname   = Column(String)
  lastname    = Column(String)
  about       = Column(String)
  isActive    = Column(Boolean)
  createdDate = Column(String)

  # TODO cleaner way? dict cevrilebilir
  def __init__(self, userCreateRequest):
    self.email       = userCreateRequest.email
    self.password    = userCreateRequest.password
    self.firstname   = userCreateRequest.firstname
    self.lastname    = userCreateRequest.lastname
    self.about       = userCreateRequest.about
    self.isActive    = False
    self.createdDate = ""

