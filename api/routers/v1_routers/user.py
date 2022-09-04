from fastapi import APIRouter, Depends, Query
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.orm import Session

from api import crud, schemas
from api.database.sqlalchemy_connection import get_session
from api.auth.auth import get_current_user, AuthService

user_router = APIRouter(
    prefix='/users',
    tags=['Users'],
    dependencies=[],
    responses={404: {'description': 'Not found'}},
)


##########

@user_router.post("/login", response_model=schemas.Token)
@user_router.post("/login/", response_model=schemas.Token, include_in_schema=False)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 session: Session = Depends(get_session),
                                 auth_service: AuthService = Depends(),
                                 ):
    user: schemas.User = auth_service.authenticate_user(session=session,
                                                        name=form_data.username,
                                                        password=form_data.password)

    access_token = auth_service.create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}


##########
@user_router.get('/me')
@user_router.get('/me/', include_in_schema=False)
async def get_user_me(current_user=Depends(get_current_user),
                      ):
    """
    **Получить данные текущего юзера.**
    """
    return current_user

##########
