from passlib.context import CryptContext
from datetime import datetime, timezone,timedelta
from jose import jwt

from app.config import (JWT_ALGORITHM,JWT_SECRET_KEY,ACCESS_TOKEN_EXPIER_MINITES)


password_context=CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password:str)->str:
    return password_context.hash(password)

def verify_password(plain_password:str, hashed_password:str)->bool:
    return password_context.verify(plain_password,hashed_password)

def create_acess_token(user_id:str, email:str)->str:
    expire_at = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIER_MINITES)
    token_data={
        "sub":user_id,
        "email":email,
        "exp":expire_at,
    }
    
    return jwt.encode(
        token_data,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )