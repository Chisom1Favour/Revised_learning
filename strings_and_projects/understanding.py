from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DatabaseConfig:
    host: str
    port: str
    user: str
    password: str
    enabled: bool = True

    def __post_init__(self):
        # Convert from environment-typical strings if needed
        if isinstance(self.port, str):
            self.port = int(self.port)
        if isinstance(self.enabled, str):
            self.enabled = self.enabled.lower() in ("true", "1", "yes")

        # Validation
        if self.port < 1 and self.port > 65535:
            raise ValueError(f"Invalid error {self.port}")
        if not self.host:
            raise ValueError("Database cannot be empty")
        if self.user and not self.password:
            raise ValueError("Password error")
        
db_config = DatabaseConfig(**raw["database"])