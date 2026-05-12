import os

raw_config = {
    "database": {
        "host": os.getenv("DB_HOST", "localhost"),
        "port": os.getenv("DB_PORT", "5432"),
        "user": os.getenv("DB_USER", "app_user"),
        "password": os.getenv("DB_PASSWORD", ""),
        "enabled": os.getenv("FEATURE_ENABLED", "True")
    },
    "redis": {
        "host": "redis.local",
        "port": 6379,
        "db": 0
    }
}