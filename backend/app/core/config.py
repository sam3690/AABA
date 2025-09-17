import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "aaba")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "aaba123")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "aaba_db")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")

    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    MONGO_DB: str = os.getenv("MONGO_DB", "aaba")

    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

settings = Settings()
