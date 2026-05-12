@dataclass(frozen=True)
class AppConfig:
    db_url: str
    api_key: str
    max_retries: int

config = AppConfig("postgresql://...", secret)