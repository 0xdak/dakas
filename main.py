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

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# creates user with given request
@app.post("/create-user", response_model=BaseResponse[UserResponse])
async def createUser(userCreateRequest: UserCreateRequest):
  print("/create-user")

  # TODO emailin valid olup olmadıgı kontrol edilecek, mail gondererek???
  if (re.fullmatch(regex, userCreateRequest.email) is False):
    info = Info(success=False, code=ERROR_CODE, message="Geçersiz Email Adresi")
    return BaseResponse(info=info)


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


# TODO user_id
@app.get("/get-user/{user_id}", response_model=BaseResponse[UserResponse])
async def getUser(id: str):
  user = db.getWithId(User, id)

  info = Info(success=True, code=100, message="Hata yok.")
  return BaseResponse(info=info, payload=user)


# auth = request.headers.get("Authorization", None)
# if not auth:
#     raise AuthError({"code": "authorization_header_missing",
#                     "description":
#                         "Authorization header is expected"}, 401)




  