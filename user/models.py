from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, DateTime

from core.db import Base


class User(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)


users = User.__table__
