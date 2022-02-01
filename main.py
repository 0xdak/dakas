from copy import deepcopy
from datetime import timedelta
from fastapi import FastAPI, Depends, status
import fastapi
from core.database.database import DatabaseManager
from core.models import *
from core.requests import *
from core.responses import *
from core import exceptions

from fastapi.security import OAuth2PasswordRequestForm
from core.security import *
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

db = DatabaseManager()
app = FastAPI()

if __name__ == "__main__":
  if (db.session is None):
    print("Failed Starting Database")
    print("Quitting...")
    exit()
    



# creates user with given request
@app.post("/create-user", response_model=BaseResponse[UserResponse], status_code=status.HTTP_201_CREATED)
async def create_user(userCreateRequest: UserCreateRequest):
  print("/create-user")
  print(userCreateRequest.__dict__)
  
  userSameEmail = db.session.query(User) \
    .filter(User.email == userCreateRequest.email) \
    .first()

  if userSameEmail is not None:
    raise exceptions.EXC_EMAIL_ALREADY_IN_USE

  #39 TODO is email valid
  #40 TODO send code to email for verifying

  if (userCreateRequest.email == '' or userCreateRequest.password == ''): # TODO cleaner with any function?
    raise exceptions.EXC_INVALID_EMAIL_OR_PASSWORD
  
  user = User(userCreateRequest = userCreateRequest)
  user.password = get_password_hash(user.password) #TODO move to User class
  # ~~saving to db
  user_orm = deepcopy(user)
  db.add(user)
  # saving to db~~
  print(user_orm.__dict__)
  userResponse = UserResponse.from_orm(user_orm)
  info = Info(success=True, code=status.HTTP_201_CREATED, message="Kullanıcı Başarıyla Oluşturuldu.")
  return BaseResponse(info=info, payload=userResponse)


@app.get("/get-user/{user_id}", response_model=BaseResponse[UserResponse])
async def get_user(user_id: str):
  print(f'/get-user/{user_id}')

  user = db.session.query(User) \
    .filter(User.userId == user_id) \
    .first()
  if user is None:
    raise exceptions.EXC_COULDNT_FIND_USER

  userResponse = UserResponse.from_orm(user)
  info = Info(success=True, code=status.HTTP_200_OK, message="Kullanıcı bulundu.")
  return BaseResponse(info=info, payload=userResponse)


# TODO -> doc 'tan denemek icin endpoint'in /token olması gerekiyor
# implementation'da /login cevrilebilir
@app.post("/token", response_model=BaseResponse[LoginResponse])
@app.post("/login", response_model=BaseResponse[LoginResponse])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
# async def login_for_access_token(form_data: LoginRequest = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
      raise exceptions.EXC_WRONG_EMAIL_OR_PASSWORD
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    loginResponse = LoginResponse(access_token=access_token, \
                                  tokenType="bearer", \
                                  userId = user.userId, \
                                  tokenExpires = access_token_expires)
    info = Info(success=True, code=status.HTTP_200_OK, message="Giriş Başarılı.")
    return BaseResponse(info=info, payload=loginResponse)


@app.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.email}]
