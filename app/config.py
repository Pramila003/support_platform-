import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME","support_platform_db")

JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM=os.getenv("JWT_ALGORITHM","HS256")
ACCESS_TOKEN_EXPIER_MINITES=int(os.getenv("ACCESS_TOKEN_EXPIER_MINITES",60))