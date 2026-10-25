from datetime import datetime ,timezone
from fastapi import APIRouter,Depends

from app.core.security import hash_password, verify_password,create_acess_token
from app.core.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from app.database import user_collection
from app.models.user import UserRegister
from fastapi.security import OAuth2PasswordRequestForm


router =APIRouter(prefix="/api/v1/auth",tags=["authentication"])

@router.post("/register")
async def register_user(user:UserRegister):
    existing_user=await user_collection.find_one(
        {"email":user.email.lower()}
    )
    
    if existing_user:
        raise UserAlreadyExistsError()
        
    new_user={
        "name":user.name,
        "email":user.email.lower(),
        "password_hash":hash_password(user.password),
        "role":"user",
        "created_at":datetime.now(timezone.utc),
        "is_active":True,
        
    }
        
    result =await user_collection.insert_one(new_user)
    return{
        "message":"User Register Successfully",
        "user_id":str(result.inserted_id),
        "email":new_user["email"]
    }
    
@router.post("/login")
async def user_login(form_data:OAuth2PasswordRequestForm=Depends()):
    email=form_data.username.lower()
    user = await user_collection.find_one(
        {"email":email}
    )
    if not user:
        raise InvalidCredentialsError()
    
    is_password_correct=verify_password(form_data.password,user["password_hash"])
    if not is_password_correct:
        raise InvalidCredentialsError()
    
    access_token = create_acess_token(
        user_id=str(user["_id"]),
        email=user["email"],
        
    )
    
    return{
        "access_token":access_token,
        "token_type":"bearer",
    }