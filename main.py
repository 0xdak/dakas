from fastapi import FastAPI
from core.models import *
from core.requests import UserCreateRequest
from core.responses import *


# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/redoc

app = FastAPI()

@app.post("/create-user", response_model=BaseResponse)
async def createUser(request: UserCreateRequest):
  print(request)

  return BaseResponse(info=info, payload=user)

@app.get("/get-user/{user_id}", response_model=BaseResponse) # TODO response_model=Response(Info, User)
async def index(user_id: str):
  info = Info(success=True, code=100, message="Hata yok.")
  user = User(username="ali", email="ali@gmail.com")
  return BaseResponse(info=info, payload=user)





# if __name__ == "__main__":

  