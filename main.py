import code
from copy import deepcopy
from distutils.log import ERROR
from email import message
from fastapi import FastAPI
from core.database.database import DatabaseManager
from core.models import *
from core.requests import UserCreateRequest
from core.responses import *
import uvicorn
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc



ERROR_CODE = 30
SUCCESS_CODE = 40

db = DatabaseManager()
app = FastAPI()

if __name__ == "__main__":
  if (db.session is None):
    print("Failed Starting Database")
    print("Quitting...")
    exit()


# creates user with given request
@app.post("/create-user", response_model=BaseResponse[UserResponse])
async def createUser(userCreateRequest: UserCreateRequest):
  print("/create-user")
  
  if (userCreateRequest.email == '' or userCreateRequest.password == ''): # TODO cleaner
    info = Info(success=False, code=ERROR_CODE, message="Email ve Şifre Alanı Boş Bırakılamaz")
    return BaseResponse(info=info)
  
  user = User(userCreateRequest = userCreateRequest)
  
  # ~~saving to db
  user_orm = deepcopy(user)
  db.add(user_orm)
  # saving to db~~
  userResponse = UserResponse.from_orm(user)
  info = Info(success=True, code=SUCCESS_CODE, message="Kullanıcı Başarıyla Oluşturuldu.")
  return BaseResponse(info=info, payload=userResponse)


# TODO user_id
@app.get("/get-user/{id}", response_model=BaseResponse[UserResponse])
async def getUser(id: str):
  info = Info(success=True, code=100, message="Hata yok.")
  user = User(username="ali", email="ali@gmail.com")
  return BaseResponse(info=info, payload=user)






  