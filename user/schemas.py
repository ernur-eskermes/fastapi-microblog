from fastapi_users import models
from pydantic import BaseModel


class User(models.BaseUser):
    class Config:
        orm_mode = True


class UserInPost(BaseModel):
    id: str

    class Config:
        orm_mode = True


class UserCreate(User, models.BaseUserCreate):
    name: str


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    pass
