import email
from fastapi import FastAPI
from core.database.database import DatabaseManager
from core.models import *
from core.requests import UserCreateRequest
from core.responses import *

# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

app = FastAPI()

@app.post("/create-user", response_model=BaseResponse[UserResponse])
async def createUser(request: UserCreateRequest):
  print("/create-user")
  # database'e kayıt edilecek
  info = Info(success=True, code=200, message="Kullanıcı başarıyla oluşturuldu.") # ??TODO
  # TODO eğer herşey tamamsa   
  
  user = User(userCreateRequest = request)
  # """
  #   USERI DB YE KAYDET
  # """
  print(user.createdDate)
  db = DatabaseManager()
  db.session.add(user)
  db.session.commit()
  userResponse = UserResponse.from_orm(user)
  db.session.close()
  return BaseResponse(info=info, payload=userResponse)

@app.get("/get-user/{user_id}", response_model=BaseResponse[UserResponse])
async def getUser(user_id: str):
  info = Info(success=True, code=100, message="Hata yok.")
  user = User(username="ali", email="ali@gmail.com")
  return BaseResponse(info=info, payload=user)





# if __name__ == "__main__":

  