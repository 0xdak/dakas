from fastapi import HTTPException, status



# /create-user
EXC_EMAIL_ALREADY_IN_USE = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail     ="Bu email adresi zaten kullanılıyor.",
)
EXC_INVALID_EMAIL_OR_PASSWORD = HTTPException(
  status_code=status.HTTP_400_BAD_REQUEST,
  detail     ="Geçersiz Email veya Şifre.",
)


# /get-user/{user_id}
EXC_COULDNT_FIND_USER = HTTPException(
  status_code=status.HTTP_400_BAD_REQUEST,
  detail     ="Kullanıcı Bulunamadı.",
)

# /token
# /login
EXC_WRONG_EMAIL_OR_PASSWORD = HTTPException(
  status_code=status.HTTP_401_UNAUTHORIZED,
  detail     ="Yanlış Email veya Şifre",
)

# get_current_user()
EXC_COULDNT_VALIDATE_CREDENTIALS = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail     ="Kimlik Bilgileri Doğrulanamadı.",
    headers={"WWW-Authenticate": "Bearer"},
)

# get_current_active_user()
EXC_INACTIVE_USER = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail     ="Inactive User.",
)