from pydantic import AnyUrl, BaseSettings, PostgresDsn, RedisDsn
import secrets


class AppSettings(BaseSettings):
    PROJECT_NAME: str = "Support Ticket"
    API_V1: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "app_"

    DATABASE_URL: PostgresDsn
    REDIS_DSN: RedisDsn = 'redis://user:pass@localhost:6379/1'
    # DATABASE_URL: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
    IS_GOOD_ENV: bool = True
    ALLOWED_CORS_ORIGINS: set[AnyUrl]


settings = AppSettings()
