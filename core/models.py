from datetime import datetime
from typing import Optional
import uuid
from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import UUID
from requests import *
from sqlalchemy import Column, String, Integer, Date, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Info(BaseModel):
  success : Optional[bool] = None
  code    : Optional[int]  = None
  message : Optional[str]  = None
  
class User(Base):
  __tablename__ = 'users'
  id          = Column(Integer, primary_key=True)
  userId     = Column(String)    # TODO UUID OLACAK
  email       = Column(String, nullable=False)
  password    = Column(String, nullable=False)
  firstname   = Column(String)
  lastname    = Column(String)
  about       = Column(String)
  isActive    = Column(Boolean)
  createdDate = Column(Date)

  # TODO cleaner way? dict cevrilebilir
  def __init__(self, userCreateRequest):
    self.email       = userCreateRequest.email
    self.password    = userCreateRequest.password
    self.firstname   = userCreateRequest.firstname
    self.lastname    = userCreateRequest.lastname
    self.about       = userCreateRequest.about
    self.isActive    = False
    self.createdDate = datetime.now()  # TODO format
    self.userId = str(uuid.uuid4())   # TODO UUID OTOMATIK OLACAK

