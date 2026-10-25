from fastapi import FastAPI ,HTTPException 
from app.database import database
import uvicorn

from app.api.auth import router as authentication

from app.core.exceptions import(
        UserAlreadyExistsError,
        user_already_exist_handler,
        InvalidCredentialsError,
        Invalid_creadentials_handler,
      
)

app=FastAPI(title="support platform")
app.include_router(authentication)


if __name__ =="__main__":
    uvicorn.run("app.main:app",host="127.0.0.1",port=8000,reload=True)
    
app.add_exception_handler(
    UserAlreadyExistsError,
    user_already_exist_handler,)
app.add_exception_handler(
    InvalidCredentialsError,
    Invalid_creadentials_handler,)

@app.get("/")
async def home():
    return {"message":"support platform is running"}

@app.get("/health")
async def health_check():
    try:
        await database.command("ping")
        return{
            "status":"healthy",
            "database":"connected"
        }
    except Exception:
        raise HTTPException(
            status_code=500 
        )

