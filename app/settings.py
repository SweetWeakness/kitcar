from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

env_path = ".env"


class Settings(BaseSettings):
    # global app settings
    app_host: str
    app_port: int

    secret_key: str

    model_config = SettingsConfigDict(env_file=env_path)


@lru_cache
def get_settings():
    return Settings()

