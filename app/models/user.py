from  pydantic  import EmailStr, BaseModel, Field

class UserRegister(BaseModel):
    name : str= Field(min_length=2, max_length=30)
    email:EmailStr
    password:str=Field(min_length=8, max_length=15)