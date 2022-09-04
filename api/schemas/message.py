from pydantic import BaseModel


class MessageBase(BaseModel):
    message: str


class CreateMessage(MessageBase):
    user_id: int


class MessageDB(MessageBase):
    id: int
    message: str | None = None
    user_id: int

    class Config:
        orm_mode = True
