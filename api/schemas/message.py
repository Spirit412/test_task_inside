from pydantic import BaseModel


class MessageBase(BaseModel):
    message: str


class GetMessage(MessageBase):
    name: str


class MessageCreate(BaseModel):
    name: str
    message: str


class MessageDB(MessageBase):
    id: int
    message: str | None = None
    user_id: int

    class Config:
        orm_mode = True
