import email
from fastapi import FastAPI
from core.models import *
from core.requests import UserCreateRequest
from core.responses import *

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

app = FastAPI()

@app.post("/create-user", response_model=BaseResponse[UserResponse])
async def createUser(userCreateRequest: UserCreateRequest):
  print("/create-user")
  # database'e kayıt edilecek
  info = Info(success=True, code=100, message="Kullanıcı başarıyla oluşturuldu.") # ??TODO
  # TODO eğer herşey tamamsa   
  print(userCreateRequest.__dict__)
  user = User(userCreateRequest)   # --> db'ye kaydedilecek
  print(user.__dict__)
  """
    USERI DB YE KAYDET
  """
  userResponse = UserResponse.from_orm(user)
  return BaseResponse(info=info, payload=userResponse)

@app.get("/get-user/{user_id}", response_model=BaseResponse[UserResponse]) # TODO response_model=Response(Info, User)
async def getUser(user_id: str):
  info = Info(success=True, code=100, message="Hata yok.")
  user = User(username="ali", email="ali@gmail.com")
  return BaseResponse(info=info, payload=user)





# if __name__ == "__main__":

  