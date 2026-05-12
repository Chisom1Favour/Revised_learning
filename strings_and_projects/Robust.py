import json
from pydantic import BaseModel, Field

class AppConfig(BaseModel):
    database_host: str = Field(alias="DB_HOST")
    database_port: int = Field(alias="DB_PORT")
    database_user: str = Field(alias="DB_USER")
    databse_password: str = Field(alias="DB_PASSWORD")

    # LOAD from JSON (could be YAML/env)
    with open("secrets.json") as f:
        file_data = json.load(f)

    config = AppConfig(**file_data)