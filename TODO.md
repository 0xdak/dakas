#1 userId Column type will be change to UUID, now it's storing as str(uuid) in string column

# ENDPOINTS (VVV -> completed, XXX -> uncompleted)
## VVV | /create-user  POST (userCreateRequest: UserCreateRequest)
    UserCreateRequest():
      email     : str
      password  : str
      firstname : str
      lastname  : str
      about     : str

    creates user:User with given userCreateRequest
    and saves it to database
    returns UserResponse 

## VVV | /get-user{userId}   GET
    takes user which's userId == given userId
    converts this to UserResponse
    returns converted UserResponse

## XXX | /login POST {loginRequest: LoginRequest}
    LoginRequest():
      email    : str
      password : str

    LoginResponse():
      token  : str
      userId : str
    
    firebase can be used.
    
    if the given values are correct, takes user in 
    returns LoginResponse
  
