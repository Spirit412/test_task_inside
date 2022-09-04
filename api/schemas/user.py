from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserUpdate(BaseModel):
    name: str

    class Config:
        orm_mode = True


class UserDB(UserBase):
    id: int
    password_digest: str | None = None

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int