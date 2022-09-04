from fastapi import HTTPException, status

###################   AUTH   ###################

EXCEPTION_EMAIL_REGISTERED = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="This email already registered.",
    headers={"WWW-Authenticate": "Bearer"}
)

EXCEPTION_EMAIL_FORMAT = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials. Bad email format.",
    headers={"WWW-Authenticate": "Bearer"}
)

EXCEPTION_PASSWORD = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials. Password verification not passed.",
    headers={"WWW-Authenticate": "Bearer"}
)

EXCEPTION_TOKEN = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Bad token.",
    headers={"WWW-Authenticate": "Bearer"}
)

EXCEPTION_EMAIL_DOESNT_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Email doesn't exists.",
    headers={"WWW-Authenticate": "Bearer"}
)

EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW-Authenticate": "Bearer"}
)


###################   SCHEMAS FIELDS VALIDATION   ###################


def raise_validation_error(field: str):
    """Поле {field} не прошло валидацию."""
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"Поле {field} не прошло валидацию.",
        headers={"WWW-Authenticate": "Bearer"}
    )


###################   ORGANIZATION VALIDATE EXCEPTIONS   ###################

def raise_logic_exception(message: str):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=message,
        headers={"WWW-Authenticate": "Bearer"}
    )


###################   USER VASLIDATE EXCEPTIONS   ###################

EXCEPTION_USER_EXISTS = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="User with this email already exists.",
    headers={"WWW-Authenticate": "Bearer"}
)
"""Пользователь с таким адресом электронной почты уже существует"""


###################   SQLALCHEMY   ###################

def raise_sqlalchemy(message: str):
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f'Ошибка БД: {message}',
        headers={"WWW-Authenticate": "Bearer"}
    )


ERROR_CONNECT_DB = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Ошибка соединения с БД',
    headers={"WWW-Authenticate": "Bearer"}
)

USER_NOT_EXISTS = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='User is not exists',
    headers={"WWW-Authenticate": "Bearer"}
)
