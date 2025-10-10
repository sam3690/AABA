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

    NATS_URL: str = os.getenv("NATS_URL", "nats://localhost:4222")

    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ROOT_USER", "aaba")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_ROOT_PASSWORD", "aaba-secret")
    MINIO_BUCKET: str = os.getenv("MINIO_BUCKET", "aaba-artifacts")

    WEAVIATE_URL: str = os.getenv("WEAVIATE_URL", "http://localhost:8080")

    OTEL_EXPORTER_OTLP_ENDPOINT: str = os.getenv(
        "OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317"
    )

    PROMETHEUS_URL: str = os.getenv("PROMETHEUS_URL", "http://localhost:9090")
    GRAFANA_URL: str = os.getenv("GRAFANA_URL", "http://localhost:3001")

    NATS_URL: str = os.getenv("NATS_URL", "nats://localhost:4222")

    MINIO_ENDPOINT: str = os.getenv("MINIO_ENDPOINT", "http://localhost:9000")
    MINIO_ACCESS_KEY: str = os.getenv("MINIO_ROOT_USER", "minio")
    MINIO_SECRET_KEY: str = os.getenv("MINIO_ROOT_PASSWORD", "minio123")
    MINIO_BUCKET: str = os.getenv("MINIO_BUCKET", "aaba-artifacts")

    WEAVIATE_URL: str = os.getenv("WEAVIATE_URL", "http://localhost:8080")

    OTEL_EXPORTER_OTLP_ENDPOINT: str = os.getenv(
        "OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317"
    )

    FLOWER_URL: str = os.getenv("FLOWER_URL", "http://localhost:5555")
    PROMETHEUS_URL: str = os.getenv("PROMETHEUS_URL", "http://localhost:9090")
    GRAFANA_URL: str = os.getenv("GRAFANA_URL", "http://localhost:3001")

settings = Settings()
