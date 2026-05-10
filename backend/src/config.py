from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


_SERVICE_ROOT = Path(__file__).resolve().parents[1]
_DEFAULT_CSV = Path(__file__).resolve().parent / "data" / "songs_spotify.csv"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_SERVICE_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    songs_csv_path: Path = _DEFAULT_CSV

    def resolved_csv_path(self) -> Path:
        path = self.songs_csv_path
        if not path.is_absolute():
            path = _SERVICE_ROOT / path
        return path


settings = Settings()
