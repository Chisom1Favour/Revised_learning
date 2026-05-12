import config
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str


@dataclass
class RedisConfig:
    host: str
    port: int
    db: int=0

with open("config.json") as f:
    raw = json.load(f)

db_conf = DatabaseConfig(**raw["database"])
redis_conf = RedisConfig(**raw["redis"])