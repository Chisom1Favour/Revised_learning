from pydantic import BaseModel, SecretStr
from pydantic.config import ConfigDict
class DataBaseConfig(BaseModel, frozen=True):
    host: str
    user: str
    password: SecretStr


# Loading from YAML
config = DataBaseConfig(host="localhost", user="admin", password="sc3rt2y")
print(config)
plain = config.password.get_secret_value()
