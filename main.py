from dataclasses import dataclass
from re import U
from typing import Generic, Optional, TypeVar

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic.generics import GenericModel

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

T = TypeVar('T')

class Info(BaseModel):
  success : Optional[bool] = None
  code    : Optional[int] = None
  message : Optional[str]  = None

#dene
class User(BaseModel):
  username : str
  email    : str

class Response(GenericModel, Generic[T]):
  info    : Info
  payload : T



app = FastAPI()

@app.get("/get-user/{user_id}", response_model=Response) # response_model=Response(Info, User)
async def index(user_id: str):
  info = Info(success=True, code=100, message="Hata yok.")
  user = User(username="ali", email="ali@gmail.com")
  return Response(info=info, payload=user)



# if __name__ == "__main__":

  