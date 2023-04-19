from pydantic import AnyUrl, BaseSettings, PostgresDsn, RedisDsn
import secrets
from functools import lru_cache


class AppSettings(BaseSettings):
    PROJECT_NAME: str
    API_V1: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    DATABASE_URL: PostgresDsn
    REDIS_DSN: RedisDsn = 'redis://user:pass@localhost:6379/1'
    IS_GOOD_ENV: bool = True
    ALLOWED_CORS_ORIGINS: set[AnyUrl]


@lru_cache()
def get_settings():
    return AppSettings()


settings = AppSettings()
