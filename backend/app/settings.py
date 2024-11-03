from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    db_username: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_drivername: str

    hash_service: str | None = None
