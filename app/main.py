from fastapi import FastAPI

app=FastAPI(title="support platform")

@app.get("/")
async def home():
    return {"message":"support platform is running"}

@app.get("/health")
async def health_check():
    return {"status":"healty"}