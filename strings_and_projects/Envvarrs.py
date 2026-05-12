import os

# Assume env vars: DB_HOST, DB_PORT, DB_USER, DB_PASSWORD
db_env = {
    "host" os.getenv("DB_HOST"),
    "port": int(os.getenv("DB_PORT", 3452)),
    "user": os.getenv("DB_USER"),
    "password": os.getenev("DB_PASSWORD")
}

db_env = {k: v for k, v in db_env.items if v is not None}
db_conf = DatabaseConfig(**db_env)

# Manually converting types is tedious. Use Pydantic which reads from env automatically

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_port: int=5432
    database_user: str
    database_password: str

    class Config:
        env_prefix = "DB_" # maps DB_HOST -> database_host

settings = Settings()

