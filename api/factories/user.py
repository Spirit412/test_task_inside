from api.auth.auth import AuthService
from api.models.models import User

from sqlalchemy.orm import Session

from api import crud, schemas
from api.crud.user_service import UserService
from api.responses.exceptions import EXCEPTION_USER_EXISTS


class UserFactory:

    def create_user(self, *,
                    session: Session,
                    user: schemas.UserCreate,
                    ):
        self.validate(session=session, user=user)
        user_service = AuthService()
        return user_service.create_user(session=session,
                                        user_data=user,
                                        )

    def validate(self, *,
                 session: Session,
                 user: schemas.UserCreate,
                 ):
        user_service = UserService()
        if user_service.get_one(session=session, name=user.name) is not None:
            raise EXCEPTION_USER_EXISTS
