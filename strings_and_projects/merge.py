defaults = {"host": "localhost", "port": 5432, "log_level": "INFO"}
file_config = {"port": 5433, "user": "admin"} # from yaml
env_config = {"log_level": "DEBUG"}  # from os.environ

# Later overries earlier
merged = {**defaults, **file_config, **env_config}
app_config = AppConfig(**merged)