from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Envs currently configured in docker-compose.yml
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    debug: bool = True
    database_url: str = "postgresql+asyncpg://user:password@localhost:5432/litestar_intro"

env = Settings() # type: ignore[call-arg]
