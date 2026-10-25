from fastapi import FastAPI ,HTTPException 
from app.database import database

app=FastAPI(title="support platform")

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
        raise HTTPExeption(
            status_code=500 
        )