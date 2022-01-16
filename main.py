import code
from copy import deepcopy
from distutils.log import ERROR
from email import message
from fastapi import FastAPI
from core.database.database import DatabaseManager
from core.models import *
from core.requests import UserCreateRequest
from core.responses import *
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc
import re


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
  userSameEmail = db.session.query(User) \
    .filter(User.email == userCreateRequest.email) \
    .first()

  if userSameEmail is not None:
    info = Info(success=False, code=ERROR_CODE, message="Bu Email Adresi Zaten Kullanılıyor.")
    return BaseResponse(info=info)

  #39 TODO is email valid
  #40 TODO send code to email for verifying

  if (userCreateRequest.email == '' or userCreateRequest.password == ''): # TODO cleaner with any function?
    info = Info(success=False, code=ERROR_CODE, message="Geçersiz Email veya Şifre.")
    return BaseResponse(info=info)
  
  user = User(userCreateRequest = userCreateRequest)
  # ~~saving to db
  user_orm = deepcopy(user)
  db.add(user)
  # saving to db~~
  print(user_orm.__dict__)
  userResponse = UserResponse.from_orm(user_orm)
  info = Info(success=True, code=SUCCESS_CODE, message="Kullanıcı Başarıyla Oluşturuldu.")
  return BaseResponse(info=info, payload=userResponse)


@app.get("/get-user/{user_id}", response_model=BaseResponse[UserResponse])
async def getUser(user_id: str):
  user = db.session.query(User) \
    .filter(User.userId == user_id) \
    .first()
  if (user is None):
    info = Info(success=False, code=ERROR_CODE, message="Kullanıcı Bulunamadı.")
    return BaseResponse(info=info)

  userResponse = UserResponse.from_orm(user)
  info = Info(success=True, code=SUCCESS_CODE, message="Kullanıcı bulundu.")
  return BaseResponse(info=info, payload=userResponse)


# auth = request.headers.get("Authorization", None)
# if not auth:
#     raise AuthError({"code": "authorization_header_missing",
#                     "description":
#                         "Authorization header is expected"}, 401)




  