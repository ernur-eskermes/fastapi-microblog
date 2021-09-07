from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase

from core.db import database
from .models import User
from .schemas import UserDB

users = User.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

SECRET = "e1c5d3789d742984e92151def479a945e905b01ffdd7275c5b2d721b4adc6b3e"

# Token 60 minutes * 24 hours * 8 days = 8 days
TOKEN_LIFETIME_SECONDS = 60 * 24 * 7

auth_backends = [
    JWTAuthentication(secret=SECRET, lifetime_seconds=TOKEN_LIFETIME_SECONDS),
]
