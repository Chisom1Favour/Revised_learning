import yaml
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DatabaseConfig:
    host: str
    port: int
    user: str
    password: str

@dataclass(frozen=True)
class AppConfig:
    db: DatabaseConfig
    max_retries: int
    enable_cache: bool

def load_config(path: Path) -> AppConfig:
    with open(path) as f:
        raw = yaml.safe_load(f)
    # Build nested frozrn dataclasses
    db = DatabaseConfig(**raw)
