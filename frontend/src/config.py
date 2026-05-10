from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


_SERVICE_ROOT = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_SERVICE_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    backend_url: str = "http://localhost:8000/api"
    request_timeout: int = 5


settings = Settings()
