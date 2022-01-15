from copy import deepcopy
from fastapi import FastAPI
from core.database.database import DatabaseManager
from core.models import *
from core.requests import UserCreateRequest
from core.responses import *
import uvicorn
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc



db = DatabaseManager()
app = FastAPI()

if __name__ == "__main__":
  if (db.session is None):
    print("Failed Starting Database")
    print("Quitting...")
    exit()
  uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)


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
  user_orm = deepcopy(user)
  db.add(user_orm)
  userResponse = UserResponse.from_orm(user)
  return BaseResponse(info=info, payload=userResponse)




@app.get("/get-user/{user_id}", response_model=BaseResponse[UserResponse])
async def getUser(user_id: str):
  info = Info(success=True, code=100, message="Hata yok.")
  user = User(username="ali", email="ali@gmail.com")
  return BaseResponse(info=info, payload=user)






  