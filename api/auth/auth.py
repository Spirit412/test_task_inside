from datetime import datetime, timedelta
from typing import Optional
import pytz
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from api.database.sqlalchemy_connection import get_session
from itsdangerous.url_safe import URLSafeTimedSerializer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import ValidationError
from sqlalchemy.orm import Session
from api import schemas
from api.config import settings
from api.crud.token import TokenService
from api.models import models
from api.responses import exceptions, success
from api.crud.user_service import UserService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")


class AuthService:

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password):
        """

        @param password:
        @return:
        """
        return pwd_context.hash(password)

    @classmethod
    def create_access_token(cls,
                            user: models.User,
                            ):
        user_data = schemas.UserDB.from_orm(user)
        timezone = 'Europe/Moscow'
        payload = {
            'name': user_data.name,
            'iat': datetime.now()
        }
        encoded_jwt = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
        return encoded_jwt

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session
        self.user_service = UserService()
        self.token_service = TokenService()

    def verify_token(self,
                     token: str = Depends(oauth2_scheme)):
        """
        Верификация токена
        @param token:
        @return:
        """
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
            if 'name' in payload:
                name: str = payload.get('name')
                if name is None:
                    raise exceptions.EXCEPTION_TOKEN
        except JWTError as e:
            raise exceptions.EXCEPTION_TOKEN
        try:
            user = self.user_service.get_one(session=self.session,
                                             name=name)
        except ValidationError as e:
            raise exceptions.EXCEPTION_TOKEN
        return user

    def authenticate_user(self, session,
                          name: str,
                          password: str):

        user = self.user_service.get_one(session=self.session,
                                         name=name)
        if not user:
            raise exceptions.EXCEPTION
        if not self.verify_password(password, user.password_digest):
            raise exceptions.EXCEPTION_PASSWORD
        return user

    def create_user(self,
                    session: Session,
                    user_data: schemas.UserCreate,
                    ):
        """
        Создание пользователя
        """
        user = models.User(name=user_data.name,
                           password_digest=self.get_password_hash(user_data.password),
                           )
        session.add(user)
        session.flush()
        return self.create_access_token(user)


def get_current_user(token: str = Depends(oauth2_scheme),
                     auth_service: AuthService = Depends(),
                     ):
    user_model = auth_service.verify_token(token=token,
                                           )
    current_user = schemas.User.from_orm(user_model)
    return current_user
