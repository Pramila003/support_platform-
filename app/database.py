from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGO_URI, DATABASE_NAME

client =AsyncIOMotorClient(MONGO_URI)
database = client[DATABASE_NAME]

user_collection =database["user"]
ticket_collection = database["ticket"]
article_collection = database["articles"]
comments_collection= database["comments"]