from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from user.schemas import UserInPost


class PostBase(BaseModel):
    title: str
    text: str


class Post(PostBase):
    id: int
    date: datetime
    user: UserInPost


class PostCreate(PostBase):
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True


class PostCreateInDB(PostCreate):
    id: int
    user: UserInPost


class PostUpdate(PostBase):
    class Config:
        orm_mode = True
