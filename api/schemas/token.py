from pydantic import BaseModel, EmailStr, Field


class Token(BaseModel):
    token: str
