#1 userId Column type will be change to UUID, now it's storing as str(uuid) in string column


# ENDPOINTS (VVV -> completed, XXX -> uncompleted)
## VVV | /create-user  POST (userCreateRequest)
  UserCreateRequest():
    email     : str
    password  : str
    firstname : str
    lastname  : str
    about     : str

    creates user:User with given userCreateRequest
    and saves it to database
    returns UserResponse 

## XXX | /get-user{userId}
    takes user which's userId == given userId
    converts this to UserResponse
    returns converted UserResponse
  
