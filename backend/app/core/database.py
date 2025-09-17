from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from pymongo import MongoClient

# Postgres
SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# MongoDB
mongo_client = MongoClient(settings.MONGO_URI)
mongo_db = mongo_client[settings.MONGO_DB]
