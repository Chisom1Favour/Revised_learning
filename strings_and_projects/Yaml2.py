import yaml
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataBaseConfig:
    host: str
    port: int
    user: str
    password: str

@dataclass(frozen=True)
class AppConfig:
    db: DataBaseConfig
    max_retries: int
    enable_cache: bool

def load_config(path: Path) -> AppConfig:
    with open(path) as f:
        raw = yaml.safe_load(f)
    db = DataBaseConfig(**raw["database"])
    return AppConfig(db=db, **raw["app"])

config = load_config("/etc/myapp/config.yaml")
